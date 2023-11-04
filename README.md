# passKeepPy

KSave is an open source project, it can help you backup your Kubernetes-YAML files.

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

![Architecture](readme-files/ksave_architecture.png)

## Installation

To activate individual virtual environment:

```bash
pip install virtualenv 
```

To create and start in project root:

```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies in virtual environment:

```bash
pip install -r requirements.txt
```

<!-- ## Usage

Every project should utilize logging, but for simple use cases, this requires a bit too much boilerplate. Instead of including all of this in your modules:
 -->


## Documentation

In this project, the [Kubernetes Python Client](https://github.com/kubernetes-client/python) proposed by kubernetes.io was used.  
Kubernetes Python Client API Endpoint List -- [Referance List](https://github.com/kubernetes-client/python/blob/36cfbe68a509d9b9d33395b22b6fa94d7d46c30f/kubernetes/README.md)  
This CLI application is coded with [arge-parse ](https://github.com/serbayacar/passkeepPy/blob/master/LICENSE.gpl).
