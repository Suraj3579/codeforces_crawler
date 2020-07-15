import requests
from bs4 import BeautifulSoup
URL = "https://www.imdb.com/list/ls057823854/"

r = requests.get(URL)
soup = BeautifulSoup(r.content,"html5lib")
movies_c = soup.find('div' , class_ = "lister-list")

movie_names = movies_c.select(".lister-item.mode-detail .lister-item-content .lister-item-header a")
names = [nm.get_text() for nm in movie_names]

movie_genres = movies_c.select(".lister-item.mode-detail .lister-item-content p.text-muted.text-small span.genre")
genres = [gn.get_text() for gn in movie_genres]

movie_times = movies_c.select(".lister-item.mode-detail .lister-item-content p.text-muted.text-small span.runtime")
runtimes = [rt.get_text() for rt in movie_times]

movie_ratings = movies_c.select(".lister-item.mode-detail .lister-item-content .ipl-rating-widget .ipl-rating-star.small span.ipl-rating-star__rating")
ratings = [ra.get_text() for ra in movie_ratings]

next_page = soup.find('a' , class_ = "flat-button lister-page-next next-page")
next_page_url = next_page['href']
URL = 'https://www.imdb.com'+ next_page_url

for i in range(99):
    
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content,"html5lib")
    movies_c = soup.find('div' , class_ = "lister-list")

    movie_names2 = movies_c.select(".lister-item.mode-detail .lister-item-content .lister-item-header a")
    names2 = [nm.get_text() for nm in movie_names2]
    names = names + names2

    movie_genres2 = movies_c.select(".lister-item.mode-detail .lister-item-content p.text-muted.text-small span.genre")
    genres2 = [gn.get_text() for gn in movie_genres2]
    genres = genres + genres2

    movie_times2 = movies_c.select(".lister-item.mode-detail .lister-item-content p.text-muted.text-small span.runtime")
    runtimes2 = [rt.get_text() for rt in movie_times2]
    runtimes = runtimes + runtimes2

    movie_ratings = movies_c.select(".lister-item.mode-detail .lister-item-content .ipl-rating-widget .ipl-rating-star.small span.ipl-rating-star__rating")
    ratings2 = [ra.get_text() for ra in movie_ratings2]
    ratingd = ratings + ratings2

    next_page = soup.find('a' , class_ = "flat-button lister-page-next next-page")
    next_page_url = next_page['href']
    URL = 'https://www.imdb.com'+ next_page_url


print(len(names))
print(len(times))
print(len(genres))
print(len(ratings))






















