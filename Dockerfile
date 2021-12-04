FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y
COPY requirements.txt /requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm

RUN cd /
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt
RUN mkdir /vc-userbot
WORKDIR /vc-userbot

COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
