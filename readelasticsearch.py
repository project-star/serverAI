from elasticsearch import Elasticsearch
import sys
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
doc=es.search(index='hypothesis', body={"query": {"match": {'renoted_id': sys.argv[1]}}})
print doc
