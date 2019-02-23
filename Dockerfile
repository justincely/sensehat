#FROM balenalib/rpi-python
FROM raspbian/jessie:latest

RUN apt-get update && apt-get install -y sense-hat python3-pip zlib1g-dev 

RUN wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz && \
    tar xzvf Python-3.6.0.tgz && \
    cd Python-3.6.0/ && \
    ./configure && \
    make -j4 && \
    make install

WORKDIR /app/

ADD . /app/

RUN pip3 install -r requirements.txt

CMD python3 hat_server.py
