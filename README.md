# BigPanda
## Task form the email:
##### Your mission in this task is to implement a deployment flow of a containerized application and it's DB:
- The deployment flow script needs to be coded using Python language (please specify which version you ran it with)
- The App + DB containers need to be run using Docker and Docker-compose:
- If you don't know docker-compose, don't worry - Go to https://docs.docker.com/compose/gettingstarted/#step-3-define-services-in-a-compose-file to view a guide on how to create a docker-compose.yml and run it.
- You DO NOT need to create any Dockerfiles, they are already given to you in the App's repo (See “About the App” section below.

##### The deployment flow script should perform the following steps:
- Download image resources file from AWS S3 (https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz) and extract it's content to '/public/images' path.
- Create, build & run the App + DB using “docker-compose up” command.
- Check the App's health (See App's healthcheck below) at the end of the deployment flow and fail the deployment flow upon bad App health.

##### Once done, please create a Github repo (Don't fork our repo) and send us a link to it. The repo should contain the following:
- The deployment flow script.
- The docker-compose.yml file.
- Any additional files needed in order to run the app from it's root folder.
- Proper documentation needed in order to fully run your exercise on our localhost.

## Result:
##### Tested on: 
```
Ubuntu 18.04.2 LTS
Python 3.6.7
Git version 2.17.1
Docker version 18.09.1, build 4c52b90
docker-compose version 1.23.2, build 1110ad01
```

##### Install Python3 and PIP
```
sudo apt update
sudo apt install -y git python3 python3-pip
```

##### Install Docker CE from docs for Ubuntu 18.04:
https://docs.docker.com/install/linux/docker-ce/ubuntu/
```
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

##### Install Docker Compose from docs for Ubuntu 18.04:
https://docs.docker.com/compose/install/
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

##### How to start:
```
git clone https://github.com/gimpel-lab/bigpanda
cd bigpanda
pip3 install -r requirements.txt
python3 deployscript.py
```


##### Structure of the project:
```
rootdir/
├── deployscript.py (The deployment flow script)
├── requirements.txt (Additional file for depensies)
├── docker-compose.yml (The docker-compose.yml file)
└── public/ (The forlder will be downloaded and unpacked from gzip from s3)
    └── images (will be mounted to ops-exercise container)
        ├── bear-2316805_1920.png
        ├── panda-1454345_1280.png
        └── panda-2850869_1920.png
```

