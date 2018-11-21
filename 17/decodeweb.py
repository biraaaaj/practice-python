#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

source=requests.get('http://ekantipur.com')
soup=BeautifulSoup(source.text,'html5lib')

for art in soup.find_all('div',class_='display-news-title'):
	fart = art.h1.a.text
	print(fart)
