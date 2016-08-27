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
        file="C:/Python27/nytimes/g2crowd/level2/"+file
        Redirect_url(file)

def Redirect_url(file):
 
  for line in open(file,'r').readlines():
    file1=line.split('/')[-2]
    filename="sub_"+file1+".csv"
    print "'filename>>>>>"+filename
    b=open(filename,'a')
    print "line...................."+line
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE
    i=1
    while(i<15):
      print line
      line = line.replace("\n", "")
      line=line+"?order=popular&page="+str(i)
      
      print line
      req = urllib2.Request(line,headers=hdr)
      htmltext = urllib2.urlopen(req).read()
      soup=BeautifulSoup(htmltext,"html.parser")
      data = soup.findAll('div',attrs={"class":"product-links"})
      i+=1
      for div in data:
        links = div.findAll('a')
        try:
          for a in links:
            c= a['href']
            path = c.split('/')[-1]
            if(path=="details"):
              print c
              b.write("https://www.g2crowd.com"+c)
              b.write("\n") 
        except:
          print "error occured" 
files_from_dir("C:/Python27/nytimes/g2crowd/level2")  #enter the absolute path of folder where your all files of g2crowd categories stored.
