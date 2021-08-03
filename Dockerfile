FROM python:3.10.0b4-alpine3.14

ENV PYTHONUNBUFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY . .

RUN adduser -D user

USER user