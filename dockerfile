FROM ubuntu:bionic-20220902

RUN apt-get update
RUN apt-get install -y firefox

RUN apt-get install python3.10 -y
RUN apt install python3-pip -y

RUN pip3 install selenium pytest

RUN apt install curl -y
RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin
