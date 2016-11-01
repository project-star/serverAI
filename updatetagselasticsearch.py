from elasticsearch import Elasticsearch
import json

def updatetags(newtags,renoted_id):
    value=json.dumps(newtags)
    print value
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    doc=es.search(index='hypothesis', body={"query": {"match": {'renoted_id': renoted_id}}})
    es.update(index='hypothesis',doc_type='annotation',id=doc["hits"]["hits"][0]["_id"],body={"doc": {"tags": value}})
    doc=es.search(index='hypothesis', body={"query": {"match": {'renoted_id': renoted_id}}})
    print doc
