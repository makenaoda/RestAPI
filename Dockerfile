FROM python:3.9.1

COPY requirements.txt requirements.txt
RUN pip install python

RUN memoriesApp.py