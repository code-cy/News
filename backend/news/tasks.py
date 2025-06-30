# default api of newsapi.prg 
# https://newsapi.org/v2/top-headlines?q=india&pageSize=20&apiKey=b32423138de3437db8273f00d5fd6053


from celery import shared_task
import requests
from django.conf import settings
import sqlite3


@shared_task
def check_update():

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "q": "india",
        "pageSize": 20,
        "apiKey": settings.API_KEY
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        DB_is_Empty(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None


def DB_is_Empty(data):
    conn = sqlite3.connect('./News/backend/db.sqlite3')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM news_toparticle')
    count = cursor.fetchone()[0]

    if count == 0:
        for article in data.get("articles", []):
            source_id = article["source"].get("id")
            source_name = article["source"].get("name") or "Unknown Source"
            author = article.get("author")
            title = article.get("title") or "Untitled Article"
            description = article.get("description")
            url_value = article.get("url")
            url_to_image = article.get("urlToImage")
            published_at = article.get("publishedAt")
            content = article.get("content")

            cursor.execute('''
                INSERT INTO news_toparticle (
                    source_id,
                    source_name,
                    author,
                    title,
                    description,
                    url,
                    url_to_image,
                    published_at,
                    content
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                source_id,
                source_name,
                author,
                title,
                description,
                url_value,
                url_to_image,
                published_at,
                content
            ))
        conn.commit()
        print("Data inserted into news_toparticle.")
    else:
        print("Table is not empty. No insertion performed.")

    conn.close()
