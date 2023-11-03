import requests
from bs4 import  BeautifulSoup
import time

                #funkcija kuria galima naudot kiytame faile

def imdb_scraper():
    headers = {
        "User-Agent": "Chrome/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    target = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    res = requests.get(target, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-59b6048d-0 jemTre cli-parent')
    new_movies_list = []
    for movie in movies:
        title = movie.find('h3', class_='ipc-title__text').text.strip()
        years = movie.find('span', class_='sc-c7e5f54-8 hgjcbi cli-title-metadata-item').text.strip()
        lenght = movie.find('div', class_='sc-c7e5f54-7 brlapf cli-title-metadata').text.strip()[4:10]
        rating = movie.find('span',
                            class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.strip().replace(
            '\xa0', ' ')[0:3]

        new_movies_list.append((title, years, lenght, rating))
    return new_movies_list

movies_list = imdb_scraper()
print(movies_list)


imdb_scraper()













