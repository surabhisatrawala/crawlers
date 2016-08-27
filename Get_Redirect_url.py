from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl
def files_from_dir(rootdir): 
  for subdir, dirs, files in os.walk(rootdir):
      print subdir
      for file in files:
      	file="C:/Python27/crawl/getapp/"+file
      	crawl_main_url(file)

def crawl_main_url(file):
	
	for line in open(file,'r'):
		print line
		line1=line.split('/')[-2]# fetch category name from url and make file with category name
		line1=line1+".csv"
		b=open(line1,'a')
		i=1
		while(i<20):
			line=line.replace("\n","")
			url=line+"?page="+str(i)
			i+=1
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
			req = urllib2.Request(url,headers=hdr)
			htmltext = urllib2.urlopen(req).read()
			soup=BeautifulSoup(htmltext,"html.parser")
			for tag in soup.find_all('a',attrs={ "class":"btn-block btn btn-raised btn-primary evnt btn-md", "data-evac":"ua_main_cta", "data-evca":"ua_click_out" ,"data-evla":"ua_serp"}):
				a= tag['href']
				print a
				b.write("https://www.getapp.com"+a)
				b.write("\n")

files_from_dir("C:/Python27/crawl/getapp")#absolute path of folder where file of all categories stored.
# a= tag.find('a')['href']