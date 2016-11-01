import json

def tagstoupdate(topwords,existingvalues):
    newtags=[]
    if existingvalues["tags"] :
	for item1 in (existingvalues["tags"]):
	    newtags.append(item1)
        print newtags
    counter=0;
    stopwords = getstopwords("stopwords1.txt")
    for item in topwords["topwords"]:
        if not (item["word"] in stopwords):
            newtags.append(item["word"])
            counter=counter+1
            if (counter==5):
                break;        
    return newtags


def getstopwords(stopwordsfilepath):
    d = []
    with open(stopwordsfilepath) as f:
        for line in f:
           d.append(line.rstrip())
    return d
