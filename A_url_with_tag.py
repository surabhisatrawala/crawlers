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
            file="C:/Python27/nytimes/applist/url/"+file

            Redirect_url(file,file1)

def Redirect_url(file,file1):
    for line in open(file,'r').readlines():
        print "line>>>>>"+line
        filename="sub_"+file1+".csv"
        print "'filename>>>>>"+filename
        b=open(filename,'a')
        # data = line.replace("\n", "")
        # url = urlparse(data)
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
            req1 = urllib2.Request(line,headers=hdr)
            htmltext1 = urllib2.urlopen(req1, context=ctx).read()
            soup = BeautifulSoup(htmltext,"html.parser") 
            for tag in soup.find_all('a',attrs={"class" : "button medium color"}): # fetch main urls
                data=tag['href']
                b.write(data+",")
                b.write("    ")
            soup1 = BeautifulSoup(htmltext1,"html.parser")  
            data = soup1.findAll('div',attrs={"class":"twelve columns"}) # fetch all tags of url
            b.write("Tags :")
            for div in data:
                links = div.findAll('a')
                for a in links:
                    if(a.text!=""):
                        print "a........."+div.text
                        b.write(a.text)
                        b.write("    ")
            b.write("\n") 
        except:
            print "error occured" 

files_from_dir("C:/Python27/nytimes/applist/url")# absolute path of folder where all files of applist are stored. 