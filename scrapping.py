from bs4 import BeautifulSoup
import requests
import lxml
from pprint import pprint


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/articles/'

def find_news(url):
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text, 'lxml')
  global_data = soup.find_all('div', class_='tm-article-snippet')
  for d in global_data:
        title = d.find('h2')
        news_link = title.find('a')['href']
        full_link = f'https://habr.com{news_link}'
        date = d.find('a', class_='tm-article-datetime-published').find('time')['title']
        key_words = d.findAll('span', class_='tm-publication-hub__link-container')
        for key in key_words:
            keys = key.find('span').text
            for k in KEYWORDS:
                if k in keys:
                    pprint(f'<{date}>-<{title.text}>-<{full_link}>')
if __name__ == '__main__':
    find_news(url)

# response = requests.get(url)
# print(response)

# bs = BeautifulSoup(response.text,"lxml")
# # print(bs)

# article_name = bs.find_all("article",class_= 'post post-prewiew')
# for article in article_name:
#   print(article_name)
