# 🗞 News Aggregator

A Django-based web application that scrapes news from major Indian news sources like NDTV, Times of India, and India Today. Articles are categorized and displayed in a beautiful UI.

## 📸 Screenshots

### 🏠 Homepage with Categorized News
![Homepage Screenshot](images/websiteUI.png)

## ⚙️ Features

- 📰 Scrapes news articles from multiple sources
- 📚 Categorizes articles automatically
- 🖥️ Responsive Bootstrap UI
- 🧠 Built with Django + BeautifulSoup + sqliteDB

## 🚀 How to Run

```bash
git clone https://github.com/your-username/news-aggregator.git
cd news-aggregator
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**## 🔁 Automating News Scraping with Task Scheduler
**To keep the news updated regularly, use the provided scrapenews.bat file and schedule it with Windows Task Scheduler.

🧾 scrapenews.bat
Create a file named scrapenews.bat like the one in the repo:
📍 Make sure to update the path "D:\News Aggregator" with your actual project path if it differs.

**Setting It Up with Windows Task Scheduler
**Open Task Scheduler (search from Start Menu).

Click Create Basic Task.

Name it something like News Scraper.

Set the trigger (e.g., Daily, or Repeat every 1 hour).

For the Action, choose Start a Program.

In Program/script, browse and select your scrapenews.bat file.

Finish the wizard.

✅ This will make sure your news scraper runs periodically and updates the site automatically.
