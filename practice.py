import os
from bs4 import BeautifulSoup
import lxml


path = os.getcwd()
html = os.path.join(path, 'index.html')

with open(html, 'r') as file:
    body = file.read()


soup = BeautifulSoup(body, "lxml")
# print(soup.prettify())


# get Title
# title = soup.title
# print(title.getText())
# # get Paragraph
# paragraph = soup.p
# print(paragraph.getText())

# # get First div
# first_div = soup.find('div')
# print(first_div.getText())

# get all the divs
# all_divs = soup.find_all('div')
# print(all_divs)

# get the First movie
# first_movie = soup.find("div", class_="movie")
# first_movie = soup.select('.movie')[0]
# print(first_movie.getText())

# get all the movies
# all_movies = soup.find_all('div', class_='movie')
# all_movies = soup.select(selector='.movie')
# for movie in all_movies:
#     print(movie.getText())

# get the links
# all_links = soup.find_all('a')
# for link in all_links:
#     print(link.get("href"))

# parent/Children

movie_box = soup.select_one("#movie-box")
# print(movie_box.getText())
parent = movie_box.find_parent()
print(parent)
# children = movie_box.children
# for child in children:
#     print(child)
