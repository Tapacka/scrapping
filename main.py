import requests
from bs4 import BeautifulSoup


KEYWORDS = {'дизайн', 'фото', 'web', 'Python', 'SQL'}
response = requests.get('https://habr.com/ru/all/')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')



articles = soup.find_all(class_='tm-article-snippet')

for article in articles:
  time_ = article.find(class_='tm-article-snippet__datetime-published')

  href = article.find(class_='tm-article-snippet__title-link')   
  final_href = href.get('href')

  title = article.find_all(class_='tm-article-snippet__title tm-article-snippet__title_h2')
  title = [art.text for art in title]
  title_ = set(title[0].split())
    
  text = article.find_all(class_='tm-article-body tm-article-snippet__lead')
  text = [art.text for art in text]
  text_=set(title[0].split())
  new_set = title_ | text_


  if new_set & KEYWORDS:
    print(f"<{title[0]}> <{time_.text}> <{final_href}>")