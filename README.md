# Oil-Wells-Crawler
This is a web crawler to download the well oils information from https://www.conservation.ca.gov/dog/Pages/Well-Search.aspx
Download the file CA Well Search Results 06-Feb-2019.xlsx which contain all of the valid well APIs
Run the following line in terminal: scrapy startproject wells 
Replace the original settings.py and items.py
Download the wellsearch_spider.py and save it to the file named spider with CA Well Search Results 06-Feb-2019.xlsx
Run the following line in terminal: scrapy crawl well_spider -o well_results.json -t json
Then the wells' status, location, operator and production will be saved to a json foramt file.
Download Aggregate_by_Operator.ipynb, install pyspark and run it.
The wells' operator which yield more than 100000000 bbl will be displayed.
