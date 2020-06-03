import re
from html import unescape
class News:
    def __init__(self, data):
        self.data = data

    def create_news_object(self):
        list_of_news = []
        for item in self.data:
            news_article = {'title': item['title'],
                            'url': item['url'],
                            'imageurl': item['imageurl'],
                            'body': unescape(item['body']),
                            'source': item['source']}
            list_of_news.append(news_article)

        return list_of_news

