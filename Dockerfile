# Version: 0.0.1
FROM ubuntu:bionic
WORKDIR /root
RUN apt update && apt install -y git vim python3 python3-pip cmake wget
RUN apt install -y build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev liblz4-dev
RUN wget https://github.com/facebook/rocksdb/archive/v5.18.3.tar.gz
RUN tar xvf ./v5.18.3.tar.gz
RUN mkdir /root/rocksdb-5.18.3/build
WORKDIR /root/rocksdb-5.18.3/build
RUN cmake ..
RUN make && make install INSTALL_PATH=/usr
WORKDIR /root
RUN git clone https://github.com/twmht/python-rocksdb.git --recursive -b pybind11
WORKDIR /root/python-rocksdb
RUN python3 ./setup.py install
RUN pip3 install pycrypto nltk flask numpy requests
WORKDIR /root
RUN git clone https://github.com/liu246542/ShieldDB
WORKDIR /root/ShieldDB
