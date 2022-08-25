import requests as req
import pandas as pd
from bs4 import BeautifulSoup
import csv
import time

# globals
main_link = # add home link
headers = {'User-agent': 'Mozilla/5.0'}

def getModels(make):
    res = req.get(make, headers=headers)
    print(res)
    models = BeautifulSoup(res.text) \
        .find('div', class_='browseby-content') \
        .findChildren('li')
    models = [main_link + model.a['href'] for model in models]
    return models

def getIssues(model):
    res = req.get(model, headers=headers)
    print(res)
    issues = BeautifulSoup(res.text) \
        .find('ul', class_='complaints worst p3') \
        .findChildren('li')
    issues = [main_link + issue.a['href'] for issue in issues]
    return issues

def getComplaints(issue):
    res = req.get(issue, headers=headers)
    print(res)
    soup = BeautifulSoup(res.text) 

    # remove unwanted
    for div in soup.find_all('div', class_=['ad', 'cheader', 'cfooter']):
        div.decompose() 
    for div in soup.find_all('p', class_='userinfo'):
        div.decompose() 

    # get complaints
    complaint_divs = soup \
        .extract('div') \
        .find_all('div', class_='complaint')

    complaints = [div.find('div', class_='comments').get_text() for div in complaint_divs]
    return complaints


def main(max_length=1000):
    # get main page
    res = req.get(main_link, headers=headers)
    soup = BeautifulSoup(res.text)

    # get makes links
    makes = soup \
        .find('section', id='mainmakes') \
        .findChildren('li') 
    makes = [main_link + make.a['href'] for make in makes]

    complaint_list = []
    with open('complaints.csv', 'w') as f:
        write = csv.writer(f)

        while len(complaint_list) < 2:
            for make in makes:
                try:
                    models = getModels(make)
                except Exception:
                    pass
                time.sleep(2)
                for model in models:
                    try:
                        issues = getIssues(model)
                    except Exception:
                        pass
                    time.sleep(2)
                    for issue in issues:
                        try:
                            complaints = getComplaints(issue)
                        except Exception:
                            pass
                        write.writerow([make] + [model] + [issue] + complaints)
                        complaint_list.extend(complaints)
                        time.sleep(2)
                        print(f'Scraped {len(complaint_list)} complaints...')
    
    print(f'Scrape complete. Scraped {len(complaint_list)} complaints')
    f.close()

    return complaint_list

if __name__ == '__main__':
    main()