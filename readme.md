# Basic scraper
Simple webscraper made to scrape complaints for Mission 3 at Mission Ready. Data was to be used in a index as part of a customer service search portal. Dumps complaints to a csv for processing with a lightweight wrangler.

1. Install dependancies
`python3 -m venv ./env`
`source ./env/bin/activate`
`pip install -r reqs.txt`
2. update `main_link` in code
3. run `scraper.py` until sufficient complaints colected
4. run `wrangler.py` to tidy up csv
