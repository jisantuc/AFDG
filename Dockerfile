FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /afdg-core
WORKDIR /afdg-core
ADD requirements.txt /afdg-core/
RUN pip install -r requirements.txt
ADD . /afdg-core/