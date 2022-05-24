FROM python:3.9.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_DIR=/app 
ENV PYTHONPATH=$PYTHONPATH:$APP_DIR
COPY requirements-dev.txt requirements.txt ./
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install -U --user pip && pip install --user -r requirements-dev.txt 

WORKDIR ${APP_DIR}
EXPOSE $PORT


CMD gunicorn app:server --bind 0.0.0.0:$PORT --preload
