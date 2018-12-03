#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import time
import csv

csv_file=open('darkhumor.csv', 'w')
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['Character','Comic Name','link'])

for num in range (5094,4490,-1):

	source=requests.get('http://explosm.net/comics/{}'.format(str(num)))
	soup=BeautifulSoup(source.text,'html5lib')

	img_src=soup.find('img',id='main-comic')['src']
	
	img_char=img_src.split('/')[4]
	img_id=img_src.split('/')[5]
	img_name=img_id.split('?')[0]

	img_link=f'https://files.explosm.net/comics/{img_char}/{img_name}'
	csv_writer.writerow([img_char,img_name,img_link])
	print(img_link) 
	time.sleep(1)
csv_file.close()

	
