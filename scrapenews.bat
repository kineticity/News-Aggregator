@echo off

REM Move to project root
cd /d "D:\News Aggregator"

REM Run scrapenews using venv's Python directly
"venv\Scripts\python.exe" newsaggregator\manage.py scrapenews >> scrape_log.txt 2>&1

echo === Scraping done ===

