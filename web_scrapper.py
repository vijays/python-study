import requests
import sys
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

links = soup.select('.titlelink')
scores = soup.select('.score')

print(links[0].getText())
print(scores[0].getText())