#-*- coding: utf-8 -*-
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl
from Gt_crawl_each_cat import line_from_file

def crawl_main_url():
	b=open("getapp.csv",'w')
 	url="https://www.getapp.com/browse"
	hdr = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
	req = urllib2.Request(url,headers=hdr)
	htmltext = urllib2.urlopen(req).read()
	soup = BeautifulSoup(htmltext,"html.parser")
	for tag in soup.find_all('a',attrs={"style" : "font-family:sans-serif;font-weight:normal;letter-spacing:0"}):
		data=tag['href']
		print data
		b.write("https://www.getapp.com"+data)
		b.write("\n")
		
crawl_main_url()
line_from_file('C:/Python27/nytimes/getapp1/getapp.csv') #calling line_from_file to crawl each category frpom getapp file












# for tag in soup.find_all("h4",attrs={"style":"margin-bottom:5px"}):
# 	file=tag.text.replace("View all","")
# 	file1=file+".csv"
# 	print "filename>>>>>>>>>>>>>>>>"+file1
# 	b=open(file1,'w')
# 	data = soup.findAll('div',attrs={"class":"block"})
# 	for div in data:
# 		links = div.findAll('a')
# 		for a in links:
# 			c= a['href']
# 			print c
#        		b.write("https://www.getapp.com"+c)
#         	b.write("\n")


