Run "G_list_cat.py" to get mapping of all the categories present in g2crowd website and stored in file named g2crowd mapping. 
command - python G_list_cat.py
-----------------------------------------------------------------
https://www.producthunt.com/

Run P1_crawl_main_url.py which fetch all categories of producthnt website and stored it in file named producthunt_cat.csv
command - python P1_crawl_main_url.py 

Run P1_crawl_each_cat.py which crawl all categories of producthunt website and stored it in file whose name based on the categories name.
command - python P1_crawl_each_cat.py 

Run P1_mainurl_with_tag.py having three functions named files_from_dir(),Redirect_url(), get_url_with_tag().
Files_from_dir() used to fetch all files from folder located in specific directory.This funtion take one argument 'rootdir' which is the absolute path of folder where all files were stored.
Redirect_url() which takes two argument file and file1.file is used to read all urls from specific file and file1 is used to make file whose name based on categories name.  
get_url_with_tag() having three arguments 'data','line' and 'file1'.'data' which is used to fetch main url of the product,
'line' is used for fetching all tags corresponding to that product url and file1 is used to store all urls and tags of the products.
command - python P1_mainurl_with_tag.py 

Run P1_list_cat.py to get mapping of all the categories present in producthunt website and stored it in file named producthunt_mapping  
