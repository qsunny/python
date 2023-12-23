# -*- codiing:utf-8 -*-

import manticoresearch
from manticoresearch.api import utils_api
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.sql_response import SqlResponse
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host="http://192.168.2.8:9308",
    server_variables={"data_dir" : "/var/lib/manticore"}
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = utils_api.UtilsApi(api_client)

    # body = "SHOW TABLES" # str  |( A query parameter string.
    # body = "CREATE TABLE products(title text, price float) morphology='stem_en'" # str  |( A query parameter string.
    body = "CREATE TABLE forum(title text, content text, author_id int, forum_id int, post_date timestamp)" # str  |( A query parameter string.
    raw_response = True # bool  | Optional parameter, defines a format of response. Can be set to `False` for Select only queries and set to `True` or omitted for any type of queries:  (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Perform SQL requests
        api_response = api_instance.sql(body)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling UtilsApi->sql: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    # try:
    #     # Perform SQL requests
    #     api_response = api_instance.sql(body, raw_response=raw_response)
    #     pprint(api_response)
    # except manticoresearch.ApiException as e:
    #     print("Exception when calling UtilsApi->sql: %s\n" % e)

