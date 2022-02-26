# ShieldDB 部署步骤

ShieldDB 是一个基于对称可搜索加密的加密数据库，本项目中包含 ShieldDB 的前端和后端组件，主要基于 Python 和 RocksDB 实现。

其中用到的 Python 库有：

+ Pycrypto (v.2.6.1)
+ NLTK (v.3.6.7)
+ Flask (v.2.0.3)
+ NumPy (v.1.19.5)
+ [python-rocksdb (v.1.0)](https://github.com/twmht/python-rocksdb)

> 注：以上第三方库除了 python-rocksdb 之外，均可以直接使用 `pip3 install [package]` 命令直接安装。

RocksDB 使用 v.5.18.3 的版本，在编译以及安装完成之后，才可以安装 `python-rocksdb` 库。

## 1. 自动部署

建议使用 `docker` 部署，容器建议使用 `ubuntu:bionic` 或相近版本。如果有 `docker` 相关基础，可以直接参考 [`Dockerfile`](./Dockerfile)，直接执行如下命令在本地编译：

```
# 使用 Dockerfile 在本地 build
# git clone https://github.com/liu246542/ShieldDB && cd ./ShieldDB
# docker build ./
```

或者直接拉取已经部署好的环境：

```
# 直接拉取已经配置好的环境
# docker pull aowatchsea/shielddb:v2
```

## 2. 手动部署

如果需要自己手动配置，参考以下步骤执行：

### 2.1. 编译 RocksDB

```
# apt install -y cmake build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev liblz4-dev
# wget https://github.com/facebook/rocksdb/archive/v5.18.3.tar.gz
# tar xvf ./v5.18.3.tar.gz
# cd rocksdb-5.18.3
# mkdir build && cd build
# cmake ..
# make && make install INSTALL_PATH=/usr
```

### 2.2. 安装 python 第三方库

使用 pip 安装常见的库

```
# pip3 install pycrypto nltk flask numpy
```

编译 python-rocksdb 库

```
# git clone https://github.com/twmht/python-rocksdb.git --recursive -b pybind11
# cd python-rocksdb
# python3 ./setup.py install
```

> 进入 python3 交互环境，如果 `import pyrocksdb` 没有问题，那么就表示安装成功。

## 3. 执行实例

将本项目 clone 到本地

```
# git clone https://github.com/liu246542/ShieldDB
```

下载需要的[数据集](https://drive.google.com/drive/folders/1e837hYzcwtxMn-IuEPFL8Uid8-ZdgqzA?usp=sharing)，分别进行解压，得到 `streaming` 和 `data256` 两个文件夹，再将这两个文件夹移动到项目根目录。

> 注：需要删除 `streaming` 文件夹中，所有后缀为 `.rsrc` 文件，即 `rm ./streaming/*.rsrc`。

开启三个终端，分别代表 `cloud server`，`padding server` 和 `client`，

+ 对于 `cloud server`，执行 `python3 ./shield_server.py`，可以看到服务器正在监听 `127.0.0.1:5000`；
+ 在服务器监听 `5000` 端口之后，模拟 `padding server` 为数据加密并上传，即执行 `python3 ./shield_stream.py`；
+ 在数据上传完成之后，模拟客户端进行查询，即执行 `python3 ./shield_search.py`，最后可以在终端看到查询关键词个数以及所花费的时间。
