FROM python:3.12
RUN mkdir /bot
WORKDIR /bot
COPY requirements.txt .
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
