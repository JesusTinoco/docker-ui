FROM alpine:latest

ADD requirement.txt requirement.txt
RUN apk add --update \
    python \
    py-pip && \
    pip install -r requirement.txt && \
    rm -rf /var/cache/apk/*

WORKDIR /docker-ui

ENTRYPOINT python run.py
