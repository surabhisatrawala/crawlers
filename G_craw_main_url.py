from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl
def crawl_main_url():
	b=open("g2crowd.csv",'a')
	url="https://www.g2crowd.com/categories"
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
	req = urllib2.Request(url,headers=hdr)
	htmltext = urllib2.urlopen(req).read()
	soup=BeautifulSoup(htmltext,"html.parser") 	
	data = soup.findAll('ul',attrs={"class":"categories-list lvl-2"})
	try:
		for div in data:
		    links = div.findAll('a')#crawl all the categories of g2crowd 
		    for a in links:
	        	c= a['href']
	        	print c
	        	b.write("https://www.g2crowd.com"+c)
crawl_main_url()

