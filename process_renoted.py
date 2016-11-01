import extracttext
import wordsfrequency
import gethypothesisvalues
import tagstoupdate
import updatetagselasticsearch
import updatepostgres
import time
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.renoted
    return db

def get_annotations(db):
    collection=db.annotations.find({"processed": False})
    for item in collection:
        print item["renoted_id"]
        extracttext.htmltotext(item["renoted_id"])
        topwords=wordsfrequency.topwords(item["renoted_id"])
        print topwords
        existingvalues=gethypothesisvalues.getExistingInfo(item["renoted_id"])
        print existingvalues
        finaltags=tagstoupdate.tagstoupdate(topwords,existingvalues)
        print finaltags
        updatetagselasticsearch.updatetags(finaltags,item["renoted_id"])
        updatepostgres.updatetags(finaltags,item["renoted_id"])
        db.annotations.update_one({'_id': item['_id']},{'$set':{"processed": True}}, upsert=False)
    return db.annotations.find({"processed": False})



def annotation_main(renoted_id):
     db = get_db()
     add_annotation(db,renoted_id)
if __name__ == "__main__":
    db=get_db()
    while(True):

        print get_annotations(db)
        time.sleep(20)
