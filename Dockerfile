FROM node:latest

EXPOSE 9000

ENV http_proxy "http://10.158.100.1:8080/"
ENV https_proxy "http://10.158.100.1:8080/"
ENV no_proxy "localhost,127.0.0.1,localaddress"

ADD . /app/
WORKDIR /app/

RUN ./install.sh
RUN python server.py &

CMD /bin/bash

