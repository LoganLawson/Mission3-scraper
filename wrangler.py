import pandas as pd

main_link = 'https://www.carcomplaints.com'
names = ['make', 'model', 'issue'] + list(range(100))
 
scraped = pd.read_csv('complaints copy.csv', names=names, header=None)
scraped = scraped.replace(main_link,'', regex=True)
scraped = scraped.replace('/','', regex=True)
scraped = scraped.replace('\n','', regex=True)
scraped = scraped.drop_duplicates(subset=['issue',0], keep='first')
scraped = scraped[0]

print(scraped)

scraped.to_csv('complaints-part.csv')

