# packer-ansible-docker-systemd
Building a Docker image running a systemd service (update message of the day) with Packer and Ansible
## Prerequisites
You will need Packer, Ansible, Docker installed on the build machine
```
apt-get install packer && apt-get install ansible && apt-get install docker
```
## Packing the image
```
packer build centos.json
```
## Running a container from the image
```
sudo docker run --privileged -dit --name=tmp --cap-add=SYS_ADMIN -e "container=docker" -v /sys/fs/cgroup:/sys/fs/cgroup:ro --tmpfs /run local:centos /usr/sbin/init
```
## Connect to the container
```
docker run -it local:centos /bin/bash
```
