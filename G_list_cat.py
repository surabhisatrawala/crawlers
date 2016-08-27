import urlparse
import urllib
from bs4 import BeautifulSoup
import re
import os
import sys
import string      
from string import ascii_lowercase

mappings = []
for i in ascii_lowercase: 
		for j in ascii_lowercase:
			mappings.append(i+j)
c=open("C:/Python27/nytimes/g2crowd/Main_urls/g2crowd_mapping.csv",'w')	#create file of nane g2crowd_mapping		
dict_name ={} 
counter = 0
for filename in os.listdir(os.getcwd()): # fetch all files from dictionary
	file= os.path.splitext(os.path.basename(filename))[0]# remove extension from file and store in file variable
	dict_name[mappings[counter]] = file # indexing of files
 	c.write(":g"+mappings[counter]+","+dict_name[mappings[counter]])#write data into file 
 	c.write("\n")
 	counter += 1
print dict_name
print len(dict_name) #len used to count the length of list