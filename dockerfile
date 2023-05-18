FROM python:3.11.3-buster

ADD . /app
WORKDIR /app

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt


CMD . venv/bin/activate && exec python automate_naukhry.py