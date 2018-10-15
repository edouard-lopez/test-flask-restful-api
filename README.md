# Test Flask RESTful API [![Build Status](https://travis-ci.org/edouard-lopez/test-flask-restful-api.svg?branch=master)](https://travis-ci.org/edouard-lopez/test-flask-restful-api)

> Minimal setup to test Flask API using Flask-RESTful and unittest

### Versions

    Flask==1.0.2
    Flask-RESTful==0.3.6


### Install

    git clone git@github.com:edouard-lopez/test-flask-restful-api.git
    cd test-flask-restful-api
    python3 -m venv env
    pip install -r requirements.txt

### Usage

    source env/bin/activate
    cd ./api/
    python3 -m unittest --verbose api.tests.test_views

One test passing :clap:

    test_GET_api_root_endpoint (api.tests.test_views.TestAPIIntegrations) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.009s

    OK