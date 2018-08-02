FROM node:latest

EXPOSE 9000

ENV http_proxy "http://10.144.1.10:8080"
ENV https_proxy "http://10.144.1.10:8080"
ENV no_proxy "localhost,127.0.0.1,localaddress,.localdomain.com,.nsn-rdnet.net"

ADD . /app/
WORKDIR /app/

RUN ./install.sh
RUN python server.py &

CMD /bin/bash
