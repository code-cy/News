# News

# 📰 News Summarizer API (Django + Gemini/OpenAI)

A simple Django-based API that fetches news from public news APIs (like NewsAPI.org), summarizes the content using AI (Gemini or OpenAI), and serves it through clean, paginated REST endpoints.

---

## 🌐 API Endpoints

### 🔍 GET `/news`

Fetch summarized news articles based on time and language.

**Query Params:**

- `time`: Date of news (e.g., `2025-12-05`)
- `lang`: Language code (e.g., `eng`)
- `limit`: Summary word limit (100, 200, or 300)

**Example:**
GET /news?time=2025-12-05&lang=eng&limit=100

### 🏠 GET `/homepage/news`

Returns top 15–20 summarized news articles for homepage display.

**Features:**

- AI Summarization via Gemini
- Supports pagination

**Query Params:**

- `page`: Page number
- `limit`: Items per page

---

## 🔐 Authentication

| Method | Endpoint    | Description          |
| ------ | ----------- | -------------------- |
| POST   | `/login`    | User login           |
| POST   | `/register` | New user signup      |
| POST   | `/refresh`  | Refresh access token |

---

## 🧠 How It Works

1. Fetch news from external APIs like `newsapi.org`
2. Use AI (Gemini / OpenAI) to summarize each article
3. Serve clean summaries through REST endpoints
4. Supports dynamic summary lengths (100, 200, 300 words)

---

## ⚙️ Tech Stack

- Django + Django REST Framework
- Gemini or OpenAI for summarization
- External APIs (NewsAPI, GNews, etc.)

---

## 📦 Setup

```bash
git clone https://github.com/yourusername/news-summarizer.git
cd news-summarizer
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
