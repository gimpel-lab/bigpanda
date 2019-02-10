#!/usr/bin/python

import os
import sys
import logging
import git
import tarfile
import urllib.request
# import requests
# import subprocess
# import time

project_directory = (os.path.dirname(os.path.realpath(__file__)))
logging_filename = project_directory + '/output.log'
git_source = 'https://github.com/bigpandaio/ops-exercise'
git_repo_name = git_source.split('/')[-1]
s3_destination_directory = project_directory + '/' + git_repo_name + '/public/images'
s3_download_url = 'https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz'


# Configure logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s  %(message)s",
    handlers=[logging.FileHandler(logging_filename), logging.StreamHandler(stream=sys.stdout)]
)


# Cloning Git
def func_git_clone(git_source, destination_dir):
    try:
        git.Git(destination_dir).clone(git_source)
    except Exception as e:
        logging.error(e)


# Git Pulling
def func_git_pull(git_source, destination_dir):
    try:
        git.Git(destination_dir).pull(git_source)
    except Exception as e:
        logging.error(e)


# Download form S3
def func_s3_download(s3_download_url, s3_destination_directory):
    try:
        stream_data = urllib.request.urlopen(s3_download_url)
        tar_data = tarfile.open(fileobj=stream_data, mode="r|gz")
        tar_data.extractall(s3_destination_directory)
    except Exception as e:
        logging.error(e)


# Update Git local repo
def func_git_update(git_source, destination_dir):
    try:
        if os.path.isdir(project_directory + '/' + git_repo_name):
            func_git_pull(git_source, destination_dir)
        else:
            func_git_clone(git_source, destination_dir)
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    func_git_update(git_source=git_source, destination_dir=project_directory)
    func_s3_download(s3_download_url, s3_destination_directory)
    print(s3_destination_directory)

