#my api key:29b38227b0594153b81c053225715d6c

import requests
from pprint import pprint

from wtforms.validators import email


class NewsFeed:
    url_base="https://newsapi.org/v2/everything?"
    api_key="GET YOUR API KEY"
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest=interest
        self.from_date=from_date
        self.to_date=to_date
        self.language=language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] +"\n"+ article['url']+"\n\n"
        return email_body

    def _get_articles(self, url):
        # get the data and construct the email
        resp = requests.get(url)
        content = resp.json()
        articles = content['articles']
        return articles

    def _build_url(self): # it is started with _ to be a private method
        # the url is obtained from newsapi.org documentation examples

        url = f"{self.url_base}" \
              f"q={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__=='main':
    news=NewsFeed(interest='nasa', from_date='2024-08-01', to_date='2024-08-20', language='en')
    print(news.get())
