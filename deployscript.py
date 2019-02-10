#!/usr/bin/python

import sys
import os
import git
import logging
# import requests
# import subprocess
# import tarfile
# import time

current_directory = (os.path.dirname(os.path.realpath(__file__)))
log_filename = current_directory + '/bigpandaio-deploy.log'

print('Log file: ', log_filename)
print('Current directory: ', current_directory)

# Printing script args
print('sys.argv = ', sys.argv)

# Checking OS version


# Checking for Docker


# Installing Docker and Docker Compose


# Checking open ports


# Cloning Git
def git_clone():
    try:
        git.Git(current_directory/ops-exercise).pull('git://github.com/bigpandaio/ops-exercise.git')
    except Exception as e:
        logging.error(e)

git_clone()

# Downloading resources


# Build Run and Compose UP


# Tests


# The deployment flow script should perform the following steps:
# Download image resources file from AWS S3 (https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz) and extract it's content to '/public/images' path.
# Create, build & run the App + DB using “docker-compose up” command.
# Check the App's health (See App's healthcheck below) at the end of the deployment flow and fail the deployment flow upon bad App health.




