import json

def tagstoupdate(topwords,existingvalues,title_headings_data):
    alltags={}
    newtags=[]
    phrasetag=[]
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
    alltags["bodytags"]=newtags
    phrasetag=phrasetags(title_headings_data,topwords)
    alltags["phrasetags"]=phrasetag        
    return alltags

def phrasetags(title_headings_data,topwords):
    val1= title_headings_data["title"]["partofspeech"]
    phrasetags=[]
    propernoun=[]
    countnoun=[]
    presenceofnumber=False
    for item in val1:
        print item[1]
        if item[1]=="NNP":
           propernoun.append(item[0])
        if item[1]=="CD":
           presenceofnumber=True
           if not ("@number" in phrasetags):
               phrasetags.append("@number")
    val2= title_headings_data["title"]["bigrams"]        
    for item in val2:
        print item
        if sublistExists(propernoun,item):
            tagval=item[0]+" " + item[1]
            phrasetags.append(tagval)
    return phrasetags
def sublistExists(big_list, small_list):
    return set(small_list).issubset(set(big_list))


def getstopwords(stopwordsfilepath):
    d = []
    with open(stopwordsfilepath) as f:
        for line in f:
           d.append(line.rstrip())
    return d
