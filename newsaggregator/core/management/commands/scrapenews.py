# core/management/commands/scrapenews.py
from django.core.management.base import BaseCommand
from core.scraper import scrape_ndtv, scrape_toi, scrape_india_today  # Import your scraping functions
import time

class Command(BaseCommand):
    help = 'Scrapes news from different sources'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting news scraping...")

        try:
            # Call your scraper functions here
            scrape_ndtv()  # Add the scrape functions for each source
            time.sleep(5)
            scrape_toi()
            time.sleep(5)

            scrape_india_today()

            self.stdout.write("News scraping completed successfully.")
        except Exception as e:
            self.stderr.write(f"Error during scraping: {str(e)}")

