#will go out to a website and will extract components and use them in your own program. 
#use the daily smarty site and have it scrape through all the data and have it return al the links that lead to post.  http://www.dailysmarty.com/topics/python
#make the link into the page title but dont grab the html in it. 
# use requests
# use inflection
# beautifulsoup

import requests as req
import inflection as inf
from bs4 import BeautifulSoup

url = 'http://www.dailysmarty.com/topics/python.html'

r = req.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup)



