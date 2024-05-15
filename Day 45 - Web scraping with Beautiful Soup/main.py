import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.findAll("h3", class_="title")

movie_titles = [title.getText() for title in titles]

movie_titles = movie_titles[::-1]

with open ("Day 45 - Web scraping with Beautiful Soup\movies.txt", "w+", encoding="utf8") as file:
    file.write('\n'.join(str(movie) for movie in movie_titles))

