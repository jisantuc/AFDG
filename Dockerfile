FROM python:2.7
ENV PYTHONUNBUFFERED 1

# set up gdal and python-gdal
RUN apt-get update
RUN apt-get install -y python-dev \
    libgdal1-dev \
    gdal-bin \
    python-gdal

# install a psql client
RUN apt-get install -y postgresql

# set up python requirements for web app
RUN mkdir /afdg-core
WORKDIR /afdg-core
ADD requirements.txt /afdg-core/
RUN pip install -r requirements.txt
ADD . /afdg-core/