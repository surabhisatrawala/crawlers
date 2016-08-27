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
  			file="C:/Python27/nytimes/Trustradius1/trust_data/"+file
  			redirect_to_mainurl(file,file1)
def redirect_to_mainurl(file,file1):
	for line in open(file,'r').readlines():
		line=line.replace("\n","")
		print line
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
			req = urllib2.Request(line,headers=hdr)
			htmltext = urllib2.urlopen(req, context=ctx).read()
			soup = BeautifulSoup(htmltext,"lxml")
			data=line.split('/')[-2]
			for tag in soup.find_all('a',attrs={"class":"vendor-backlink"}):
				data=tag['href']
				print "data......................"+data
			tag_url(line,file1,data)
		except:
			print "error ocurred"	

def tag_url(line,file1,data):
	filename="sub_"+file1
	b=open(filename,'a')
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		    'Accept-Encoding': 'none',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Connection': 'keep-alive'}
	ctx = ssl.create_default_context()
	ctx.check_hostname = False 
	ctx.verify_mode = ssl.CERT_NONE
	req1 = urllib2.Request(line,headers=hdr)
	htmltext1 = urllib2.urlopen(req1, context=ctx).read()
	soup1 = BeautifulSoup(htmltext1,"lxml")
	try:
		for tag in soup1.find_all('a',attrs={"class":"btn btn-primary"}):
			tag_data=tag.text
			if(tag_data!="Are You a Software Vendor?"):
				tag_data2=tag_data.split(' ')[0]
				if(tag_data2!="Compare"):
					tag_data1=tag_data.split('vs.')[-2]
					print "data....."+tag_data1
					b.write("url:"+data+",")
					b.write('tag:'+"  "+tag_data1)
					b.write("\n")
				else:
					tag_data=tag_data.replace('Compare','')
					print "data....."+tag_data
					b.write("url:"+data+",")
					b.write('tag:'+"  "+tag_data)
					b.write("\n")
	except:
		print "error........"
files_from_dir("C:/Python27/nytimes/Trustradius1/trust_data")			 					

