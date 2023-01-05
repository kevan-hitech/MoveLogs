# MoveLogs
Automatically move logs from Syslog server local directory to AWS s3 bucket

# Requirements

AWS CLI - https://aws.amazon.com/cli/


#Accessing the AWS bucket
In order for the script to access the AWS bucket via AWS CLI, credentials will need to be provided

Create root configuration profile that AWS CLI can use
 aws configure --profile wasabi



Edit the following variables if needed. 

INTERVALS = [How many days before the next check]
BASE_PATH = [Location of original logs]
BUCKET_PATH_ = [Location of buckets] 
