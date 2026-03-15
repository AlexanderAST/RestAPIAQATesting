FROM python:3.10-alpine3.19

RUN apk update && \
    apk add --no-cache openjdk11-jre curl tar && \
    curl -o /tmp/allure.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxf /tmp/allure.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/local/bin/allure && \
    rm -rf /tmp/allure.tgz

WORKDIR /usr/workspace

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt