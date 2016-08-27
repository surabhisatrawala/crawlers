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
      f=open(rootdir+"/"+file,'r') #use the absolute URL of the file
      urls_to_load = f.readlines()
      exit
      i+=1
      fle = file
      # print fle
      res = fetch_parallel(urls_to_load,fle)
      exit
      b=open("sub_"+file,'a')
      
      responseList = []
      for items in range(0, res.qsize()):
          b.write(res.get_nowait())
      # b.write(responseList)
      b.close()     
      #for line in lines:
        #ssl_conn(line,file)

def ssl_conn(line,file,queue): # for ssl support and redirect url to its main site url
  print line
  line = line.replace("\n", "")
  url=line+"/visit"
  url1 = urlparse(line)
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
    req = urllib2.Request(url,headers=hdr)
    req.headers['Range'] = 'bytes=%s-%s' % (0, 1836)
    htmltext = urllib2.urlopen(req,context=ctx).geturl()
    print "text.........."+htmltext
    queue.put(htmltext+"\n")
  except:
    print "error occured"
   
def fetch_parallel(urltoread,filename):
  # print  fle
  result = Queue.Queue()
  threads = [threading.Thread(target=ssl_conn, args = (url,filename,result)) for url in urltoread]
  for t in threads:
      t.start()
  for t in threads:
      t.join()
  return result 

files_from_dir("C:/Python27/nytimes/Beta_list/markets")# absolute path where category file of market stored.
