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
c=open("C:/Python27/nytimes/getapp1/cat/getapp_mapping.csv",'w')			
dict_name ={} 
counter = 0
for filename in os.listdir(os.getcwd()): 
	file= os.path.splitext(os.path.basename(filename))[0]
 	c.write(file)
 	c.write("\n")
 	counter += 1
print dict_name
print len(dict_name) 
