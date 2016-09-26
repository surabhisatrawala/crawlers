https://www.getapp.com/browse

Run Gt_crawl_main_url.py which is used to fetch all the categories present in getapp website and store in file name getapp.csv.After that line from file function were called which cral each category of getapp file automatically and stored it in file name corresponding to their category name.
command - python Gt_crawl_main_url.py  

Run Gt_redirect_to_mainurl.py having three functions
named files_from_dir(), Redirect_url(), main_url().
Files_from_dir() is used to fetch each file from specific directory mentioned in an argument name 'rootdir' which is the path of specific directory.
Redirect_url() is used to fetch all the line whose redirect url of main product we get and then main_url() funtion is called where it fetch all the main url of the product, otherwise it fetch main url of the product present in specifications of each product.
command  - python Gt_redirect_to_mainurl.py 

Run Gt_list_cat.py to get mapping of all the categories present in getapp website ans stored it in file named getapp_mapping.
command python Gt_list_cat.py
