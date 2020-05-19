scrapy-http-pipeline
==========================

[![Build Status](https://travis-ci.com/thecodecook/scrapy-http-pipeline.svg?branch=master)](https://travis-ci.com/thecodecook/scrapy-http-pipeline)
[![Requires.io](https://requires.io/github/thecodecook/scrapy-http-pipeline/requirements.svg?branch=master)](https://requires.io/github/thecodecook/scrapy-http-pipeline/requirements?branch=master)

Just a simple Scrapy HTTP pipeline to POST your items to your server.

## Usage

### Install

```
pip install scrapy-http-pipeline
```

### Configure scrapy settings.py

```
ITEM_PIPELINES = {
    'scrapyhttppipeline.scrapyhttppipeline.HttpPostPipeline': 500
}

# Url to your server, which accepts POST requests
HTTP_POST_PIPELINE_URL = 'localhost:8080/items'

# Any custom headers you want to add, e.g. authentication
HTTP_POST_PIPELINE_HEADERS = {
    'X-Authorization': 'xxx'
}
```

## Developing

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

### Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

### Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.3-3.7, should you choose to use it.
