FROM ubuntu:14.04.update

MAINTAINER landers chen

COPY . /opt/test/

RUN pip install pyyaml

WORKDIR /opt/test

EXPOSE 9090

CMD ["python", "web.py"]

