# -*- codiing:utf-8 -*-
import os

# from __future__ import print_function

import time
import manticoresearch
from manticoresearch import *
from manticoresearch.rest import ApiException
from pprint import pprint

"""Matplotlib绘图实用的小技巧 添加标题"""
__author__ = "aaron.qiu"


"""
pip install manticoresearch
"""

if __name__ == "__main__":
    # Defining the host is optional and defaults to http://127.0.0.1:9308
    # See configuration.py for a list of all supported configuration parameters.
    configuration = manticoresearch.Configuration(
        host="http://192.168.2.8:9308"
    )

    # Enter a context with an instance of the API client
    with manticoresearch.ApiClient(configuration) as api_client:
        # Create an instance of the IndexApi API class
        api_instance = manticoresearch.IndexApi(api_client)
        # body = "["'{\"insert\": {\"index\": \"test\", \"id\": 1, \"doc\": {\"title\": \"Title 1\"}}},\\n{\"insert\": {\"index\": \"test\", \"id\": 2, \"doc\": {\"title\": \"Title 2\"}}}'"]"  # str |

        # try:

            # Bulk index operations
            # api_response = api_instance.bulk(body)
            # pprint(api_response)
        # except ApiException as e:
        #     print("Exception when calling IndexApi->bulk: %s\n" % e)

        # Create an instance of the Search API class
        api_instance = manticoresearch.SearchApi(api_client)

        # Create SearchRequest
        search_request = SearchRequest()
        search_request.index = 'chips_product'
        search_request.fullltext_filter = QueryFilter('Title 1')

        # The example passes only required values which don't have defaults set
        try:
            # Perform a search
            api_response = api_instance.search(search_request)
            pprint(api_response)
        except manticoresearch.ApiException as e:
            print("Exception when calling SearchApi->search: %s\n" % e)