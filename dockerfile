FROM ubuntu:bionic-20220902
RUN apt-get update && apt-get install -y firefox
CMD /usr/bin/firefox