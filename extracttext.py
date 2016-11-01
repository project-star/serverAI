import urllib
import sys
from bs4 import BeautifulSoup

def htmltotext(renoted_id):

    filepath= "alldocs/"+renoted_id+".html"
    f = open(filepath,'r')

    htmltext = f.read()
    f.close
    soup = BeautifulSoup(htmltext)

# kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

# get text
    text = soup.get_text()

# break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    filepath = "alldocs/processed/"+renoted_id+".txt"
    f = open(filepath,'w')
    f.write(text.encode('ascii', 'ignore').decode('ascii'))
    f.close()
#print(text)
if __name__ == "__main__":

    print "success"
