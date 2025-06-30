import requests
from django.conf import settings
import os
from news.models import TopArticle
from django.utils.dateparse import parse_datetime

def save_articles():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "q": "india",
        "pageSize": 20,
        "apiKey": os.environ.get("NEWS_API")
    }
    try:
        response = requests.get(url= url, params=params, timeout=10)
        response.raise_for_status()
        response_data = response.json()
    except Exception as e:
        return f"Error fetching news: {e}"
    for article in response_data["articles"]:
        TopArticle.objects.create(
            source_id=article["source"].get("id"),
            source_name=article["source"].get("name", ""),
            author=article.get("author"),
            title=article.get("title", ""),
            description=article.get("description"),
            url=article.get("url"),
            url_to_image=article.get("urlToImage"),
            published_at=parse_datetime(article.get("publishedAt")),
            content=article.get("content"),
        )






# @shared_task
# def check_update():

#     url = "https://newsapi.org/v2/top-headlines"
#     params = {
#         "q": "india",
#         "pageSize": 20,
#         "apiKey": settings.API_KEY
#     }
#     try:
#         response = requests.get(url, params=params, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         DB_is_Empty(data)
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching news: {e}")
#         return None


# def DB_is_Empty(data):
#     conn = sqlite3.connect('./News/backend/db.sqlite3')
#     cursor = conn.cursor()

#     cursor.execute('SELECT COUNT(*) FROM news_toparticle')
#     count = cursor.fetchone()[0]

#     if count == 0:
#         for article in data.get("articles", []):
#             source_id = article["source"].get("id")
#             source_name = article["source"].get("name") or "Unknown Source"
#             author = article.get("author")
#             title = article.get("title") or "Untitled Article"
#             description = article.get("description")
#             url_value = article.get("url")
#             url_to_image = article.get("urlToImage")
#             published_at = article.get("publishedAt")
#             content = article.get("content")

#             cursor.execute('''
#                 INSERT INTO news_toparticle (
#                     source_id,
#                     source_name,
#                     author,
#                     title,
#                     description,
#                     url,
#                     url_to_image,
#                     published_at,
#                     content
#                 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#             ''', (
#                 source_id,
#                 source_name,
#                 author,
#                 title,
#                 description,
#                 url_value,
#                 url_to_image,
#                 published_at,
#                 content
#             ))
#         conn.commit()
#         print("Data inserted into news_toparticle.")
#     else:
#         print("Table is not empty. No insertion performed.")

#     conn.close()
