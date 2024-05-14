# Meraki Log Uploader

## Overview

This Python script automates the process of uploading Meraki system logs from a local server to an AWS S3 bucket. It is designed to run continuously, checking at defined intervals whether it is time to initiate the upload process. The script includes functionality to rename the log files with a date stamp before uploading them, ensuring that each upload is uniquely identifiable and organized chronologically.

## Features

- **Automated Uploads:** Logs are automatically uploaded at regular intervals.
- **Renaming Logs:** Log files are renamed with a date stamp reflecting the range of logs they contain.
- **System Restart:** The system logging service is restarted after each upload to ensure continued log capture without interruption.
- **Debug Mode:** Includes a debug mode for testing that increases the frequency of checks and uploads.

## Requirements

- Python 3.x
- AWS CLI installed and configured with appropriate AWS credentials
- Access to the server where Meraki logs are stored

## Setup and Configuration

1. **Clone the Repository:**


2. **Install Dependencies:**
Ensure you have Python 3.x installed and the AWS CLI configured on your system. The AWS CLI must be configured with credentials that have permission to write to the specified S3 bucket.

3. **Configure Script Settings:**
Open the script and adjust the following settings according to your environment:
- `DEBUG`: Set to `True` for debugging (increases check frequency).
- `BASE_PATH`: Set to the directory path where the logs are located.
- `BUCKET_PATH_BRK` and `BUCKET_PATH_DWN`: Set to the S3 bucket paths where logs will be uploaded.

## Usage

To start the script, run:
```python meraki_log_uploader.py```


The script runs in an infinite loop, checking if it's time to upload the logs and performing the upload if so. The upload interval can be adjusted by changing the `INTERVAL` setting in the script.

## Logging

The script prints messages to the console about its operations, including when it checks for the next upload time and when it uploads a file. These messages can help in monitoring the script's activity.



Edit the following variables if needed. 

INTERVALS = [How many days before the next check]
BASE_PATH = [Location of original logs]
BUCKET_PATH_ = [Location of buckets] 
