import urllib2,cookielib
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import Queue
import threading
import re
import os
import sys
import ssl
responseList =[]
def files_from_dir(rootdir): 
  for subdir, dirs, files in os.walk(rootdir):
      responselist=[] 
      print subdir
      for file in files:
      	f=open(rootdir+"/"+file,'r') #use the absolute URL of the file
      urls_to_load = f.readlines()
      print urls_to_load
      print "\n"
      fle = file
      res = fetch_parallel(urls_to_load,fle)
      print "res........."+ str(res)
      filename="sub_"+fle
      b=open(filename,'a')
      for items in responseList:
        print "item./.............."+items
        if items!="":
          b.write("url :"+items+","+"tags :"+fle)
          b.write("\n")

      #b.write()
     	#b.close()     

def Redirect_url(line,file,queue):
  
  #print "responselist.........."+responseList
  line = line.replace("\n", "")
  url = urlparse(line)
  filename="sub_"+file+".csv"
  
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE
  req = urllib2.Request(line, headers=hdr)
  req.headers['Range'] = 'bytes=%s-%s' % (0, 1836)
	#htmltext = urllib2.urlopen(req, context=ctx).geturl()
  try:
    page = urllib2.urlopen(req,context=ctx)
  except urllib2.HTTPError, e:
    print e.fp.read()
  content = page.read()
  soup = BeautifulSoup(content,"html.parser")
  data = soup.find('script')
  #   b.write(responseList)
  for n in data:#soup.find_all('script'):
    n = n[n.find('http'):n.find('")')]
    print "n........"+n
    responseList.append(str(n))

def fetch_parallel(urltoread,filename):
  result = Queue.Queue()
  threads = [threading.Thread(target=Redirect_url, args = (url,filename,result)) for url in urltoread]

  for t in threads:
      t.start()
  for t in threads:
      t.join()
  return result 

files_from_dir("C:/Python27/crawl/getapp")#set the absolute path of the folders where all file of categories were stored