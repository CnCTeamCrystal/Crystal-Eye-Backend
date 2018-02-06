#-*- coding: utf-8 -*-
from __future__ import print_function
import json
from watson_developer_cloud import DiscoveryV1


discovery = DiscoveryV1(
    version='2017-11-07',
    username='fa6ca473-2c4a-4222-828a-066ae905c664',
    password='UNLBvDbEbE1S')

"""
response = discovery.create_environment(
    name="my_environment",
    description="My environment",
    size=1
)

print(json.dumps(response, indent=2))

"""

environments = discovery.list_environments()
print(json.dumps(environments, indent=2))


news_environments = [x for x in environments['environments'] if x["name"] == 'Watson System Environment']

news_environment_id = news_environments[0]['environment_id']
#print(json.dumps(news_environment_id, indent=2))

collections = discovery.list_collections(news_environment_id)
news_collections = [x for x in collections['collections']]
print(json.dumps(collections, indent=2))

configurations = discovery.list_configurations(
    environment_id=news_environment_id)
print(json.dumps(configurations, indent=2))

query_options = {'query': 'Samsung'}
query_results = discovery.query(news_environment_id,
                                news_collections[0]['collection_id'],
                                query_options)

print(json.dumps(query_results, indent=2))

