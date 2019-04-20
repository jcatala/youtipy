from bs4 import BeautifulSoup
import requests

def search(q):
    r = requests.get('https://www.youtube.com/results?search_query={}'.format(q))
    soup = BeautifulSoup(r.text,features="html.parser")
    d = {}
    # Having html parsed, lets run on it
    id = 0
    for k in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        d[id] = [k['title'] , "https://www.youtube.com{}".format(k['href']) ]
        id += 1
    return d



