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
        file1 = file # file1 is used to make file whose name based on corresponding catgeories
        file="C:/Python27/nytimes/Producthunt_crawl/cat/"+file # path where files were stored.
        Redirect_url(file,file1)

def Redirect_url(file,file1):
  for line in open(file,'r').readlines():#read each line from file
    print "line>>>>>"+line
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
    soup = BeautifulSoup(htmltext,"html.parser")   
    for tag in soup.find_all('div',attrs={"class":"actions_vQA0Z"}):#fetch redirect url 
      data= tag.find('a')['href']
      print "....Redirect_data...."+data #redirect url
      get_url_with_tag(data,line,file1)

def get_url_with_tag(data,line,file1):
    filename="sub_"+file1+".csv"
    print "'filename>>>>>"+filename
    b=open(filename,'a')
    data = data.replace("\n", "")
    url = urlparse(data)
    try:
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib2.Request(url.geturl(),headers=hdr)
        req.headers['Range'] = 'bytes=%s-%s' % (0, 1836)# send request header
        htmltext = urllib2.urlopen(req, context=ctx).geturl()
        req1 = urllib2.Request(line,headers=hdr)
        htmltext1 = urllib2.urlopen(req1, context=ctx).read()
        print "....data...."+htmltext # fetch main url from redirect url
        b.write(htmltext+",")
        b.write("  ")
        soup1 = BeautifulSoup(htmltext1,"html.parser")  
        data = soup1.findAll('div',attrs={"class":"topicWrap_2Uvaj"})# to find all tags of corresponding main url 
        b.write("Tags :")
        for div in data:
            print div.text
            if(div.text!=""):# remove empty tags 
                print "a........."+div.text
                b.write(div.text)
                b.write("    ")
        b.write("\n") 
    except:
        print "error occured"           


files_from_dir("C:/Python27/nytimes/Producthunt_crawl/cat")#give absolute path of folder where all files were stored