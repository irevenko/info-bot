from newsapi import NewsApiClient
from secrets import NEWS_TOKEN

api = NewsApiClient(api_key=NEWS_TOKEN)


def get_article():
    author = api.get_top_headlines(sources='bbc-news')['articles'][0]['author']
    title = api.get_top_headlines(sources='bbc-news')['articles'][0]['title']
    description = api.get_top_headlines(sources='bbc-news')['articles'][0]['description']
    url = api.get_top_headlines(sources='bbc-news')['articles'][0]['url']
    time = api.get_top_headlines(sources='bbc-news')['articles'][0]['publishedAt']
    time = time.replace('T', ' ')[:20]
    content = api.get_top_headlines(sources='bbc-news')['articles'][0]['content']
    content = content.split('.')[0]
    article = f'✏️ <b>Auhtor</b>:  {author}\n⚠️ <b>Title</b>:  {title}\n📝 <b>Description</b>:  {description}\n📌 <b>In short</b>:  {content}\n🕒 <b>Published at</b>:  {time}\n➡️ <b>Full article</b>:  {url}'
    return article
    