import urllib
import sys
from bs4 import BeautifulSoup
from textblob import TextBlob
import json
def title_headings_data(renoted_id):

    filepath= "alldocs/"+renoted_id+".html"
    f = open(filepath,'r')

    htmltext = f.read()
    f.close
    soup = BeautifulSoup(htmltext)



# kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out


# extract title of page
    print "title of page"
    print soup.title.string


# extract element of headings

#    headingsdata('h1',soup)
    extradata=headingsdata('title',soup)
#    headingsdata('h3',soup)
#    headingsdata('h4',soup)
#    headingsdata('h5',soup)
#    headingsdata('h6',soup)
    return extradata 

def headingsdata(tagtype,soup):
    for element in soup.select(tagtype):
        value={}
        text=element.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        wiki = TextBlob(text)
        value["partofspeech"]=wiki.tags
        value["bigrams"]=wiki.ngrams(n=2)
        value["trigrams"]=wiki.ngrams(n=3)
        value1={}
        value1[tagtype]=value
        return value1
