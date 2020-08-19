import json

import requests
from scrapy.utils.serialize import ScrapyJSONEncoder
from twisted.internet.threads import deferToThread

default_serialize = ScrapyJSONEncoder().encode


class HttpPostPipeline(object):
    settings = None
    items_buffer = []

    def __init__(self, url, headers=None, serialize_func=default_serialize):
        """Initialize pipeline.
        Parameters
        ----------
        url : StrictRedis
            Redis client instance.
        serialize_func : callable
            Items serializer function.
        """
        self.url = url
        self.headers = headers if headers else {}
        self.serialize_func = serialize_func

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        params = {
            'url': settings.get('HTTP_POST_PIPELINE_URL'),
        }
        if settings.get('HTTP_POST_PIPELINE_HEADERS'):
            params['headers'] = settings['HTTP_POST_PIPELINE_HEADERS']

        return cls(**params)

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):
        data = self.serialize_func(item)
        requests.post(self.url, json=json.loads(data), headers=self.headers)
        return item
