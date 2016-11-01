from flask import Flask
from flask import json
import uuid
from flask_cors import CORS, cross_origin
from flask import request
from lxml import html
import subprocess
import shlex
import os
import json
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import mechanize
import nltk
from bs4 import BeautifulSoup
from html2text import html2text 
import re
import mongodb


app = Flask(__name__)
CORS(app)
@app.route('/sendmsg', methods=['POST'])
def api_message():
    print request.headers
    data=json.dumps(request.json)
    #print data
    #print request
    msg= request.json["msg"].encode('ascii', 'ignore').decode('ascii')
    id= str(request.json["annot"])
    soup = BeautifulSoup(msg)
    soup =soup.encode('ascii', 'ignore').decode('ascii')
    filepath = "alldocs/"+id+".html"
    f = open(filepath, "w")
    f.write( soup  )      # str() converts to string
    f.close()
    mongodb.annotation_main(id)
#    id = request.json["annot"]
    #tree = html.fromstring(msg.content)
#    parser = MyHTMLParser()  
#    print msg 
#    print id
#    parser.feed(msg)
    #print parser.data
  #  renoted_id = str(uuid.uuid4())
    return id


@app.route('/addbookmark', methods=['POST'])
def add_bookmark():
    print request
    print request.headers
    data=json.dumps(request.json)
    print data
    print request.json
    uri= request.json["uri"]
    title= request.json["title"]
#    mongodb.annotation_main(id)
#    id = request.json["annot"]
    #tree = html.fromstring(msg.content)
#    parser = MyHTMLParser()  
#    print msg 
#    print id
#    parser.feed(msg)
    #print parser.data
  #  renoted_id = str(uuid.uuid4())
    return "success"

def run_command(cmd):
    cmd = shlex.split(cmd)
    return subprocess.check_output(cmd).decode('ascii')

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr

    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
        print "Data     :", data

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data


class MyHTMLParser2(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0 
    self.noteinfo = 0
    self.data = []
    self.counter = 0;
  def handle_starttag(self, tag, attrs):
    if tag == 'div':
      for name, value in attrs:
        if name == 'class' and value == 'PIAeditable PIAcontent':
          print name, value
          print "Encountered the beginning of a %s tag" % tag 
          self.recording = 1
          self.counter +=1 
    if tag == 'title':
      self.noteinfo = 1


  def handle_endtag(self, tag):
    if tag == 'div' or tag == 'title':
       self.recording =0 
       self.noteinfo = 0;
       print "Encountered the end of a %s tag" % tag 

  def handle_data(self, data):
    
    if self.recording:
      item = {"id": self.counter, "value": data}
      self.data.append(item)
    if self.noteinfo:
      item = {"title" : data}
      self.data.append(item)


if __name__ == "__main__":
    app.run('0.0.0.0',port=5010)

