import requests
from bs4 import BeautifulSoup
from .models import NewsArticle

def get_category_from_url(url):
    """
    Extract category from the URL based on predefined keywords.
    """
    if 'india-news' in url or '/india/' in url:
        return 'India News'
    elif 'education' in url:
        return 'Education'
    elif 'sports' in url:
        return 'Sports'
    elif 'business' in url:
        return 'Business'
    elif 'world' in url:
        return 'World'
    elif 'gadgets360' in url or 'science' in url:
        return 'Technology'
    else:
        return 'General'
def scrape_ndtv():
    url = "https://www.ndtv.com/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Select all article blocks
    articles = soup.select("body > div.vjl-cnt > div > div > div > div:nth-child(1) > article")

    for article in articles[:10]:  # Limit to top 10 articles
        title_tag = article.select_one("div > div > div > ul > li:nth-child(1) > div > div > div > h2 > a")
        summary_tag = article.select_one("div > div > div > ul > li:nth-child(2) > div > div > div > p")
        link = title_tag.get("href") if title_tag else None

        if title_tag and link:
            title = title_tag.get_text(strip=True)
            summary = summary_tag.get_text(strip=True) if summary_tag else ""
            full_link = "https://www.ndtv.com" + link if not link.startswith("http") else link
            category=get_category_from_url(full_link)
            print(category)

            NewsArticle.objects.get_or_create(
                title=title,
                summary=summary,
                url=full_link,
                source='NDTV',
                category=category
            )



def scrape_toi():
    url = "https://timesofindia.indiatimes.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Select all article anchors
    article_links = soup.select("div.QeV0F ul li a")

    for article in article_links[:10]:  # Top 10 only
        title_tag = article.select_one("div.UreF0 > p.CRKrj")
        summary_tag = article.select_one("div.UreF0 > p.W4Hjm")
        link = article.get("href")

        if title_tag and link:
            title = title_tag.get_text(strip=True)
            summary = summary_tag.get_text(strip=True) if summary_tag else ""
            full_link = (
                link if link.startswith("http") 
                else "https://timesofindia.indiatimes.com" + link
            )
            category=get_category_from_url(full_link)
            print(category)

            NewsArticle.objects.get_or_create(
                title=title,
                summary=summary,
                url=full_link,
                source='TOI',
                category=category

            )


def scrape_india_today():
    url = "https://www.indiatoday.in/top-stories"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Select all article blocks
    article_blocks = soup.select("div.B1S3_content__wrap__9mSB6")

    for block in article_blocks[:10]:
        title_tag = block.select_one("h2 > a")
        summary_tag = block.select_one("div.B1S3_story__shortcont__inicf > p")

        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.get("href")
            summary = summary_tag.get_text(strip=True) if summary_tag else ""
            full_link = (
                link if link.startswith("http") 
                else "https://www.indiatoday.in" + link
            )
            category=get_category_from_url(full_link)
            print(category)

            NewsArticle.objects.get_or_create(
                title=title,
                summary=summary,
                url=full_link,
                source='India Today',
                category=category

            )


def run_all_scrapers():
    scrape_ndtv()
    scrape_toi()
    scrape_india_today()
