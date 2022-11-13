FROM ubuntu:bionic-20220902

RUN apt-get update
RUN apt-get install -y firefox

RUN apt-get install python3.10 -y
RUN apt install python3-pip -y
RUN apt-get install -y python3-tk

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

RUN apt install curl -y
RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin
