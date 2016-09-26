from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl

def line_from_file(file): # take each line from file and process
  	for line in open(file,'r').readlines():# open each url of  Betalistcat_crawl file line by line
  		if(line!=" "):
	  		print "lines......................."+line
	  		path = line.split('/')[-1] #take last part of url define category and put in path variable
	  		path=path.replace("\n", "")
	  		os.makedirs(path) 
	  		filename = path + '.csv'
	  		crawl_main_url(line,path,filename)
		
	
def crawl_main_url(line,path,filename):
	with open(os.path.join(path, filename), 'w') as b:
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
		req = urllib2.Request(line,headers=hdr)
		htmltext = urllib2.urlopen(req).read()
		soup=BeautifulSoup(htmltext,"html.parser")
		for tag in soup.find_all('a',attrs={"tag tag--card"}):
			a= tag['href']
			print a
		 	b.write("https://betalist.com"+a)
		 	b.write("\n")

line_from_file("C:/Python27/nytimes/Beta_list/MainPage_crawl.txt")	# crawl MainPage_crawl file contain market and region category	 	
		
	
