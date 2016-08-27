from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl

  
def line_from_file(file): # take each line from file and process 
  i=0
  for line in open(file,'r').readlines(): # open each url of market file line by line  
    i +=1
    print line
    path = line.split('/')[-1] #take last part of url define category of market and put in path variable
    path=path.replace("\n", "") 
    filename = path + '.csv' # create file of path name with .txt extension 
    print filename
    crawl_data(path,filename,line)

def crawl_data(path,filename,line): #take url to crawl 
  print line
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive'}
  req = urllib2.Request(line,headers=hdr)
  htmltext = urllib2.urlopen(req).read()
  soup_func(path,filename,htmltext)

def soup_func(path,filename,htmltext): #parse url through beautiful soup and store data in file
  with open(filename ,'w') as b:
    soup = BeautifulSoup(htmltext,"html.parser")
    for tag in soup.find_all('div',attrs={"class" : "startup startupGridItem"}):# take url of class startupGridItem_name
      data=tag.find('a')['href']
      print data
      b.write("https://betalist.com"+data) #write data into file
      b.write("\n")

line_from_file('C:/Python27/nytimes/Beta_list/markets/markets.csv') # crawl market cat file and make changes in folder name if u want to crawl file of region folder 