https://www.trustradius.com/

Run "T_crawl_main_url.py" to get all the categories and sub_categories of that website and stored it in file named trust_cat.
command - python T_crawl_main_url.py

Run "T_Redirect_url" to fetch all the categories, crawl that categories in sequence and stored crawl categories in a file accordingly.We need to specify absolute path of that folder where file of categories i.e trust_cat stored.
command - python T_Redirect_url.py

Run "T_redirect_to_mainurl.py" it give main url and list of competitors of the particular product.Product whose main urls are not mentioned fetch keyword of that product along with its competitors.
command - python T_redirect_to_mainurl.py
