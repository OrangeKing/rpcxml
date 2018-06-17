FROM node:latest

EXPOSE 9000

ADD . /app/
WORKDIR /app/

RUN ./install.sh
RUN python server.py &

CMD /bin/bash
