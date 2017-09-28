FROM continuumio/anaconda3:4.2.0

WORKDIR /container
ADD ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install --upgrade -I setuptools && \
    pip install --ignore-installed -r requirements.txt

ADD credentials.json .

ADD ./src ./src
