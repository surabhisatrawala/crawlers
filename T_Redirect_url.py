#-*- coding: utf-8 -*-
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl

def files_from_dir(rootdir):
  for subdir, dirs, files in os.walk(rootdir): 
      for file in files:
        file1 = file
        file="C:/Python27/crawl/trustradius/sub_folder/"+file
        Redirect_url(file,file1)

def Redirect_url(file,file1):
  for line in open(file,'r').readlines():
    print "line>>>>>"+line
    line=line.replace("\n","")
    line1=line.split('/')[-1]
    line1=line1.split('#')[-2]
    line1=line1+".csv"
    b=open(line1,'a')

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib2.Request(line,headers=hdr)
    htmltext = urllib2.urlopen(req, context=ctx).read()
    try:
        soup = BeautifulSoup(htmltext,"lxml")
        for tag in soup.find_all('a'):
            data= tag['href']
            data1=data.split('/')[-1]
            if(data1=="competitors"):
                data="https://www.trustradius.com"+data
                print "....data...."+data
                b.write("https://www.trustradius.com"+data)
                b.write("\n")
    except:
        print "error ocureed"            
    
files_from_dir("C:/Python27/crawl/trustradius/sub_folder")            