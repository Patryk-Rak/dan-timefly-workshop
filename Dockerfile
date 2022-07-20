FROM python:3.10-bullseye
LABEL maintainer="dan-timefly-workshop.com"

ENV PYTHONUNBUFFED 1

COPY ./requirements.txt /requirements.txt
COPY ./core /core

WORKDIR /core
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home core-app-user


ENV PATH="/py/bin:$PATH"

USER core-app-user