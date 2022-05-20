FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /betterstore
ADD . /betterstore
RUN pip install -r requirements.txt




