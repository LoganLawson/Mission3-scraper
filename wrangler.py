import pandas as pd

def main():
    main_link = # add home link
    names = ['make', 'model', 'issue'] + list(range(100))

    scraped = pd.read_csv('complaints copy.csv', names=names, header=None)
    scraped = scraped.replace(main_link,'', regex=True)
    scraped = scraped.replace('/','', regex=True)
    scraped = scraped.replace('\n','', regex=True)
    scraped = scraped.drop_duplicates(subset=['issue',0], keep='first')

    print(scraped)

    scraped.to_csv('complaints-wrangled.csv')

if __name__ == '__main__':
    main()

