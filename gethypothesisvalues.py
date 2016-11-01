from elasticsearch import Elasticsearch


def getExistingInfo(renoted_id):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    doc=es.search(index='hypothesis', body={"query": {"match": {'renoted_id':renoted_id}}})
    id=doc["hits"]["hits"][0]["_id"]
    tags=doc["hits"]["hits"][0]["_source"]["tags"]
    selector=doc["hits"]["hits"][0]["_source"]["target"][0]["selector"]
   #es.update(index='hypothesis',doc_type='annotation',id=doc["hits"]["hits"][0]["_id"],body={"doc": {"tags": ["pakistan","india","movies"]}})
    value={"id":id,"tags":tags,"selector":selector}
    return value


