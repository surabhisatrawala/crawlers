#-*- coding: utf-8 -*-
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl

url="https://www.getapp.com"
b=open("getapp.csv",'w')
#url1=urlparse(url)
hdr = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
req = urllib2.Request(url,headers=hdr)
htmltext = urllib2.urlopen(req).read()
#print htmltext
soup = BeautifulSoup(htmltext,"html.parser") 
for tag in soup.find_all('a',attrs={"class" : "bigger-tap-target"}):
	data=tag['href']
	data="https://www.getapp.com"+data
	print data
	b.write(data) #write data into file
	b.write("\n")

