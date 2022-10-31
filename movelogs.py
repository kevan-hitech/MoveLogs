from datetime import datetime, timedelta
import os
import time
import subprocess


def checktime(lastcheck,timenow):
    """Check if it is the correct time to iniiate script"""

    if lastcheck is None:
        lastcheck = timenow
    lastcheck_ = lastcheck.split(" ")
    lc_date = lastcheck_[0].split("-")
    lc_hour = lastcheck_[1]
    lastcheck_dt = datetime(int(lc_date[0]),int(lc_date[1]),int(lc_date[2]),int(lc_hour))

    delta = lastcheck_dt + timedelta(days=INTERVAL)
    delta = delta.strftime("%Y-%m-%d %H")

    message = "Now: [%s]\nNext Check: %s" % (timenow, delta)
    print(message)

    if timenow == delta:
        return True
    else:
        return False

def getfiledate():
    """Format for when a file was generated to its last log"""

    today_ = (datetime.now())
    before_ = (datetime.now()) - timedelta(days=INTERVAL)
    today_ = today_.strftime("%Y-%m-%d")
    before_ = before_.strftime("%Y-%m-%d")

    title = "%s_to_%s_" % (before_,today_)

    return title

def command(input_):
    """Pipe command to the terminal"""

    input_ = input_.split(" ")
    command_ = subprocess.run(input_, 
                        stdout=subprocess.PIPE, 
                        universal_newlines=True)
    
    if DEBUG:
        print(command_)
    return (command_)

def upload(log_path,bucket_path):
    """Create rename log"""

    # Rename
    new_path = getfiledate() + log_path
    #os.rename(BASE_PATH + log_path, BASE_PATH + new_path)
    rename_command = "sudo mv %s/%s %s/%s" % (BASE_PATH,log_path, BASE_PATH,new_path)
    rename = command(rename_command)
    
    # Restart sys log to resume logging
    restart_command = "sudo /etc/init.d/syslog-ng restart"
    restart = command(restart_command)

    # Upload log 
    upload_command = "aws s3 cp %s/%s %s/%s --profile wasabi --endpoint-url=https://s3.wasabisys.com" % (BASE_PATH,new_path, bucket_path,new_path)
    upload = command(upload_command)

    return new_path

# ---------------------------------------------------------------

# Testing (True) or Prod (False)
DEBUG = True

# Path of logs
BASE_PATH = "/var/log"
BUCKET_PATH_BRK = "s3://meraki-syslogs-test/Logs/Brooklyn"
BUCKET_PATH_DWN = "s3://meraki-syslogs-test/Logs/Downtown"

# How often logs will be uploaded 
INTERVAL = 1

# Initial interval checks
lastchecked = None

if DEBUG:
    lastchecked = "2022-10-30 20"
    INTERVAL = 1


if __name__ == "__main__":

    while True:
        # Get the time right now ex: 2022-10-31 15 ()
        currently = (datetime.now()).strftime("%Y-%m-%d %H")
        print(currently)
        
        # If time matches - initiate
        if checktime(lastchecked,currently):
            upload("meraki_BRK.log",BUCKET_PATH_BRK)
            upload("meraki_DWN.log",BUCKET_PATH_DWN)

            lastchecked = (datetime.now()).strftime("%Y-%m-%d %H")
            
            time.sleep(3600)

        # Check again in 60 seconds 
        else:
            time.sleep(60)


