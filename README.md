# python_demo_service

### PreRequirements

- pyenv installed
- python 3.6.7

### Install Dependent Packages

```
pyenv activate env_grpc_demo
pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

### Gen demo.proto to python grpc code

```
./build.sh
```

### Run Server

```
python server.py
```

### Run Client

```
python client.py
```
