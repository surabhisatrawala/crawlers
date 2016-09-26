#-*- coding: utf-8 -*-
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl
from Gt_redirect_to_mainurl import files_from_dir

def line_from_file(file): 
  os.makedirs("cat") 
  path="cat"
  if os.path.exists("cat"):
    i=0
    for line in open(file,'r').readlines(): 
      i +=1
      print line
      path1= line.split('/')[-2] # split the last part of line 
      path1=path1.replace("\n", "") 
      filename = path1 + '.csv'# make file name based on the category name.
      print "filename"+filename
      crawl_data(path,filename,line)

def crawl_data(path,filename,line): 
  print line
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive'}
  req = urllib2.Request(line,headers=hdr)
  htmltext = urllib2.urlopen(req).read()
  soup_func(path,filename,htmltext)
  


def soup_func(path,filename,htmltext): 
  with open(os.path.join(path, filename), 'w') as b: # open file in cat directory to write data in it. 
    soup = BeautifulSoup(htmltext,"html.parser")
    for tag in soup.find_all('a',attrs={"class" : "evnt","data-evac":"ua_facet","data-evca":"ua_facet_categories","data-evla":"ua_serp"}):# fetch all the urls of each category
      data=tag['href'] 
      print data
      b.write("https://www.getapp.com"+data) 
      b.write("\n")

  # files_from_dir("C:/Python27/nytimes/getapp1/cat")     
