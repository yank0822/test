FROM ubuntu:14.04

MAINTAINER landers chen

COPY . /opt/test/

RUN apt-get update && apt-get install -y \
        python-pip && \
    pip install pyyaml

WORKDIR /opt/test

EXPOSE 9090

CMD ["python", "web.py"]

