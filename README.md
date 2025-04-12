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

## 🔁 Automating News Scraping with Task Scheduler

To keep the news updated regularly, use the provided `scrapenews.bat` file and schedule it with **Windows Task Scheduler**.

### 🧾 scrapenews.bat

Create a file named `scrapenews.bat` like the one in the repository
📍 Make sure to update the path "D:\News Aggregator" with your actual project path if it differs.

### 🗓 Setting It Up with Windows Task Scheduler

Follow these steps to automate your scraping script:

1. **Open Task Scheduler** (search for it in the Start Menu).
2. Click **Create Basic Task** on the right panel.
3. **Give your task a name**, like `News Scraper`.
4. **Set the Trigger**:
   - Choose **Daily**, or  
   - Select **One Time** and configure **Advanced Settings** to repeat every hour or as needed.
5. **Set the Action**:
   - Choose **Start a Program**.
   - In the **Program/script** field, **browse and select your `scrapenews.bat` file**.
6. Click **Finish** to schedule the task.

✅ Your scraper will now run automatically at the configured intervals and keep your site up to date!
