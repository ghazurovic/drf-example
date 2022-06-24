FROM python:3.9-alpine3.15

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk upgrade \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache postgresql-dev

RUN python3 -m ensurepip && pip3 install --upgrade pip setuptools wheel

COPY ./requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

RUN apk del build-deps

COPY ./docker-entrypoint.sh /usr/local/bin/entrypoint
RUN ["chmod", "+x", "/usr/local/bin/entrypoint"]

EXPOSE 8000

ENTRYPOINT /usr/local/bin/entrypoint
