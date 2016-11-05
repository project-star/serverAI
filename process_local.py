import extracttext
import extracttext_extrafeatures
import wordsfrequency
import textblobprocess
#import gethypothesisvalues
import tagstoupdate
#import updatetagselasticsearch
#import updatepostgres
import time
import sys
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


def local_annotations(renoted_id):
    extracttext.htmltotext(renoted_id)
    topwords=wordsfrequency.topwords(renoted_id)
    title_headings_data=extracttext_extrafeatures.title_headings_data(renoted_id)
    print topwords
    print title_headings_data
    existingvalues={}
    existingvalues["tags"]=[]
    print existingvalues
    finaltags=tagstoupdate.tagstoupdate(topwords,existingvalues,title_headings_data)
    print finaltags

def annotation_main(renoted_id):
     db = get_db()
     add_annotation(db,renoted_id)
if __name__ == "__main__":
        local_annotations(sys.argv[1])
        
