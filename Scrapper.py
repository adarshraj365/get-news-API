import requests
import lxml
import bs4
import io
import time,datetime
from urllib.error import HTTPError,URLError
from requests.exceptions import ConnectionError

import json


def get_news(category):
	    #category = ""
	    newDictonary = {
	        'category': category,
	        'success': True,
	        'data': []
	    }
	    try:
	        print('https://inshorts.com/en/read'+"/"+category)
	        htmlBody = requests.get('https://inshorts.com/en/read/' + category)
	    except requests.exceptions.RequestException as e:
	        newDictonary['success'] = False
	        newDictonary['error'] = str(e.message)
	        return newDictonary
	    # Soup object
	    soup = bs4.BeautifulSoup(htmlBody.text, 'lxml')
	    newscard = soup.find_all(class_='news-card')
	    if not newscard:
	        newDictonary['success'] = False
	        newDictonary['error'] = 'Invalid Category'
	        return newDictonary
	    for card in newscard:
	        try:
	            title = card.find(class_="news-card-title").find('a').text
	        # print(title)
	        except:
	            title = None
	
	        try:
	            author = card.find(class_="news-card-author-time").find(class_='author').text
	        # print(author)
	        except:
	            author = None
	
	        try:
	            content = card.find(class_="news-card-content").find('div').text
	        # print(content)
	        except:
	            content = None
	
	        try:
	            news_link = card.find(class_="read-more").find('a').get('href')
	        # print(news_link)
	
	        except:
	            news_link = None
	
	        dict = {
	            'title': title,
	            'author': author,
	            'content': content,
	            'news_link': news_link
	        }
	
	        newDictonary['data'].append(dict)
	    return newDictonary


print("hello")
#dict = get_news('https://inshorts.com/en/read')
dict = get_news("sports")

info = dict['data']

for i in range(len(info)):
	print(info[i])
	print("######################")