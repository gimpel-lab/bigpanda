#!/usr/bin/env python3

import os
import sys
import logging
import tarfile
import urllib.request
import subprocess
from time import sleep

project_directory = (os.path.dirname(os.path.realpath(__file__)))

s3_destination_directory = project_directory + '/public/images'
s3_download_url = 'https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz'

health_check_url = 'http://localhost:3000/health'
health_check_retries = 10
health_check_timeout = 6

logging_filename = project_directory + '/output.log'
logging_level = logging.INFO
logging_format = '%(asctime)s %(name)s: %(message)s'


logging.basicConfig(
    level=logging_level,
    format=logging_format,
    handlers=[logging.FileHandler(logging_filename), logging.StreamHandler(stream=sys.stdout)]
)


def func_s3_download(s3_download_url, s3_destination_directory):
    logging.info('Downloading:' + s3_download_url + 'to:' + s3_destination_directory)
    try:
        tarfile.open(fileobj=urllib.request.urlopen(s3_download_url), mode="r|gz").extractall(s3_destination_directory)
    except Exception as e:
        logging.error(e)
        sys.exit(e)


def func_exec_shell(*args):
    logging.info('Executing:' + str(args))
    try:
        subprocess.call([*args])
    except Exception as e:
        logging.error(e)
        sys.exit(e)


def func_health_check(health_check_url):
    logging.info('Starting health check')
    for retry in range(health_check_retries):
        try:
            health_check_status = urllib.request.urlopen(health_check_url).getcode()
        except Exception as e:
            health_check_status = 0
        if health_check_status == 200:
            logging.info('Health check is ok')
            return True
        logging.error('Health check fail, retries:' + str(retry + 1) + '/' + str(health_check_retries))
        sleep(health_check_timeout)
    return False


def main():
    func_s3_download(s3_download_url, s3_destination_directory)
    func_exec_shell('docker-compose', 'rm', '--stop', '--force')
    func_exec_shell('docker-compose', 'up', '-d', '--force-recreate')
    if func_health_check(health_check_url):
        logging.info('Success deploying the app')


if __name__ == "__main__":
    logging.info('Starting deploy flow')
    main()
