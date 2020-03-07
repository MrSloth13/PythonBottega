import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))

    return titles


r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)




#notes
"""
Okay so i definatly would say i failed at this just by how far off i was on some of the things i needed to do. ONE VERY IMPORTANT THING IS WHEN YOU ARE DEALING 
WITH A BEAUTIFUL SOUP OBJECT IS YOU CAN TREAT IT LIKE A DICTIONARY AND USE [] TO FIND THE STUFF YOU WANT. I COULD HAVE MADE THIS SO MUCH SIMPLIER. 
"""