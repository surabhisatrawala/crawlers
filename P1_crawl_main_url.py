from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl

url="https://www.producthunt.com/"
b=open("producthunt_cat.csv",'w')
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
req = urllib2.Request(url,headers=hdr)
htmltext = urllib2.urlopen(req).read()
soup=BeautifulSoup(htmltext,"html.parser")
for tag in soup.findAll('a',attrs={"class":"item_1k3Lx"}):# crawl all categories of producthunt
	print tag['href']
	a=tag['href']
	b.write('https://www.producthunt.com'+a)
	b.write("\n")

       