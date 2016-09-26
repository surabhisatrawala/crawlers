from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl

def line_from_file(file):
  i=0
  for line in open(file,'r').readlines():
    i +=1
    print line
    path = line.split('/')[-1] # split the last part of the url
    path=path.replace("\n", "") # replace the new line function with space 
    filename = path + '.csv' # make file name based on category name
    print filename
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
  with open(filename ,'w') as b:
    soup = BeautifulSoup(htmltext,"html.parser")
    for tag in soup.find_all('a',attrs={"class" : "link_3fUGJ"}):
      data=tag['href']
      print data
      b.write("https://www.producthunt.com"+data) 
      b.write("\n")

# line_from_file('C:/Python27/nytimes/Producthunt_crawl/producthunt_cat.csv')
