FROM ubuntu:bionic-20220902

RUN apt-get update
RUN apt-get install -y firefox

RUN apt-get install python3.10 -y

CMD python3 /home/app/main.py