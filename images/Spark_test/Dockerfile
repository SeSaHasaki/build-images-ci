FROM ubuntu:16.04

MAINTAINER 814537706@qq.com

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y openssh-client openssh-server && \
    apt clean