#will go out to a website and will extract components and use them in your own program. 
#use the daily smarty site and have it scrape through all the data and have it return al the links that lead to post.  http://www.dailysmarty.com/topics/python
#make the link into the page title but dont grab the html in it. 
# use requests
# use inflection
# beautifulsoup

# One important thing i have noticed is all of the links that lead to an actuall post are in h2 tags. all the rest of the items are just in an a tag while the links we want are in h2's

import requests as req
import inflection as inf
from bs4 import BeautifulSoup
import pprint

url = 'http://www.dailysmarty.com/topics/python'

page = req.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

page_content = []
for i in range(10):
    titles = soup.find_all("h2")[i]
    page_content.append(titles)

h2_soup = BeautifulSoup(str(page_content), features=('html.parser'))

tags = h2_soup.find_all('a')

post_links = []

for tag in tags:
    post_links.append(tag.get('href'))

for post_link in post_links:
    trimmed_link = post_link[7:]
    underscored_link = inf.underscore(trimmed_link)
    human_list = inf.humanize(underscored_link)
    titled_list = inf.titleize(human_list)
    print(titled_list)
    






