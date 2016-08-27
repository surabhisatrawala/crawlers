from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import re
import os
import sys
import ssl
import Queue
import threading

urls_to_load = ""
fle = ""
def files_from_dir(rootdir): #take each file from directory and process each line of file 
  i=0
  for subdir, dirs, files in os.walk(rootdir): 
      for file in files:
        f=open(rootdir+"/"+file,'r') #use the absolute path of the file
        urls_to_load = f.readlines()
        responseList=[]
        exit
        i+=1
        fle = file
        res = fetch_parallel(urls_to_load,fle)
        exit

def ssl_conn(line,file,queue):# for ssl support and redirect url to its main site url

  line = line.replace("\n", "")
  url = urlparse(line)
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
  except:
  	print "got error in header"
  try:
    req = urllib2.Request(url.geturl(),headers=hdr)
    req.headers['Range'] = 'bytes=%s-%s' % (0, 1836)
    htmltext = urllib2.urlopen(req, context=ctx).read()
    soup = BeautifulSoup(htmltext,"html.parser")   
    for tag in soup.find_all('dl',attrs={"class":"small-dl"}):
      data= tag.find('a')['href']
      print "...."+data
      data=str(data)
      b=open(file,'a')
      b.write(data)
      b.write("\n")
      b.close()
      # queue.put(data+"\n")
  except:
  	print "...error occured...."

def fetch_parallel(urltoread,filename):
  result = Queue.Queue(maxsize=500)
  urltoread = urltoread[:500]
  threads = [threading.Thread(target=ssl_conn, args = (url,filename,result)) for url in urltoread]
  for t in threads:
      t.start()
  for t in threads:
      t.join()
  return result

files_from_dir("C:/Python27/crawl/g2crowd/level3") #enter the absolute path of folder where your files are stored