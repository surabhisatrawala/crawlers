https://betalist.com/

Run "B_craw_main_url.py" to get the categories of markets and regions whose urls are stored in file named MainPage_crawl.
command - python B_craw_main_url.py


Run "B_crawl_each_cat.py" to fetch and crawl all the categories of markets and regions.To crawl the categories of regions and markets we need to give absolute path of folder where markets or regions file are stored.
command - python B_crawl_each_cat.py

Run "B_Redirect_to_mainurl.py" which fetch all the main urls of the market and region categories.In calling we need to mention absolute path of folder where all files of this categories were stored.
command - python B_Redirect_to_mainurl.py
