from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text

soup = BeautifulSoup(contents,"html.parser")

print("Headings:")
headings = soup.find_all(name="span",class_ = "titleline") 
for heading in headings:
    print(heading.getText())


print("Scores:")
scores = soup.find_all(name="span",class_ = "score")
for score in scores:
    print(score.getText())

print("Links in headings:")
links = soup.find_all(name="span",class_ = "titleline")
for link in links:
    print(link.a.get("href"))