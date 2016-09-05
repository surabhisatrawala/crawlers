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
			file1=file
			file="C:/Python27/nytimes/getapp1/cat/"+file
			Redirect_url(file,file1)

def Redirect_url(file,file1):
	file1="sub_"+file1
	print "filename>>>>>"+file1
	for line in open(file,'r'):
		url = line.replace("\n", "")
		try:
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
			ctx = ssl.create_default_context()
			ctx.check_hostname = False
			ctx.verify_mode = ssl.CERT_NONE
			req = urllib2.Request(url,headers=hdr)
			htmltext = urllib2.urlopen(req,context=ctx).read()
			soup=BeautifulSoup(htmltext,"html.parser")
			for tag in soup.find_all('a',attrs={"class":"btn btn-primary btn-block btn-lg evnt","data-evac":"ua_main_cta"}):
				if(tag.text=="Visit Website"):
					tag['href']
					link = "https://www.getapp.com"+tag['href']
					main_url(link,file1)
				b=open(file1,'a')	
				if(tag.text=="Compare App"):
					data = soup.find_all('ul',attrs={"class":"nav nav-pills nav-stacked"})
					for div in data:
					    links = div.findAll('a')
					    for a in links:
				        	c= a['href']
				        	if(c=="#specifications"):
				        		for tag in soup.find_all('a',attrs={"class":"text-muted"}):
				        			tags=tag.text.replace("Back to Top","")
				        			if(tags!=" "):
				        				print "tags>>>>>>"+tags
				        				b.write(tags)
				        				b.write("\n")
		except:
			print "error occured"	        				


def main_url(link,file1):
	b=open(file1,'a')
	link = link.replace("\n", "")
	url = urlparse(link)
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	req = urllib2.Request(url.geturl(),headers=hdr)
	req.headers['Range'] = 'bytes=%s-%s' % (0, 1836)
	try:
		page = urllib2.urlopen(req,context=ctx)
	except urllib2.HTTPError, e:
		print e.fp.read()
	try:	
	  	content = page.read()
	  	soup = BeautifulSoup(content,"html.parser")
	  	data = soup.find('script')
	  	for n in data:#soup.find_all('script'):
	   		n = n[n.find('http'):n.find('")')]
	    	print "n........"+n
	    	b.write(n)
	    	b.write("\n")
	except:
		print "error occured"    	
files_from_dir("C:/Python27/nytimes/getapp1/cat")