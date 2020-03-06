#will go out to a website and will extract components and use them in your own program. 
#use the daily smarty site and have it scrape through all the data and have it return al the links that lead to post.  http://www.dailysmarty.com/topics/python
#make the link into the page title but dont grab the html in it. 
# use requests
# use inflection
# beautifulsoup

import requests as req
import inflection as inf
from bs4 import BeautifulSoup
import pprint

url = 'http://www.dailysmarty.com/topics/python'

page = req.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# <div class="full-width-div">
# <div class="card">
# <div class="col-mid-12">
# <div class="post-item-wrapper">
links = soup.find('div', class_="full-width-div")

print(links.prettify())



