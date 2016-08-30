https://www.g2crowd.com/categories

Run "G_craw_main_url.py" to fetch all the categories and sub-categories of g2crowd and then manually create files of all categories.
command python G_craw_main_url.py 

Run "G_Redirect_url.py" fetch all the files from folder name level2 which contain categories of g2crowd.Then it give all the redirect urls of that categories and then manually create folder named level3 and store all files of redirect urls.
command - python G_Redirect_url.py

Run "G_redirect_to_mainurl.py" which give all the main urls of the product.We need to specify the folder i.e level3 where all files of redirect urls were stored.
command - python G_redirect_to_mainurl.py

Run "G_list_cat.py" to get mapping of all the categories present in g2crowd website and stored in file named g2crowd mapping. 
command - python G_list_cat.py
