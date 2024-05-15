from bs4 import BeautifulSoup
import requests
import re #because I can't for the life of me find out where in the HackerNews page the so called storylink class is! If the page changes, wonderful. Otherwise, at May 7th 2024, I CANNOT find this class and it's driving me nuts!


response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article = soup.find(class_="titleline")

# article_link = article.get_text()

# print (article)
# url = re.search(r'href="([^"]*)"', str(article)).group(1)
# formatted_article = f'"{url}"'
# print (formatted_article)

articles = soup.findAll(class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    title_text = article_tag.get_text()
    article_texts.append(title_text)
    url = re.search(r'href="([^"]*)"', str(article_tag)).group(1)
    article_links.append(url)
article_upvotes = [int(score.getText().replace(" points", "")) for score in soup.findAll(name="span", class_="score")]

# print (article_texts, article_upvotes, article_links, sep="\n")
# print (len(article_texts), len(article_upvotes), len(article_links), sep="\n")

max = max(article_upvotes)

index = article_upvotes.index(max)

print (article_texts[index], article_links[index], sep="\n")