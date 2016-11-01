#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import json

con = None

def updatetags(finaltags,renoted_id):
    counter=0
    value="{" + finaltags[0]
    for item in finaltags:
        counter=counter+1
        if counter > 1:
            value=value+","+item
    value=value+"}"
    print value
    try:
     
        con = psycopg2.connect(host='localhost',user='postgres') 
        cur = con.cursor()
        query="update annotation set tags='"+ value+"' where extra->>'renoted_id' = '"+ renoted_id +"';"
        print query
        cur.execute(query)
        #cur.execute("update annotation set tags='{pakistan,india,movies}' where extra->>'renoted_id' = '1475389750893';")          
        con.commit()
     
    

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
    
    
    finally:
    
        if con:
            con.close()
