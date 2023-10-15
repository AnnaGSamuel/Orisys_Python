from bs4 import BeautifulSoup
file = open("index.html")
contents = file.read()
file.close()
print(contents)

soup = BeautifulSoup(contents,"html.parser")

print(soup)
print(soup.prettify())
print(soup.title) 
print(soup.h1)

print(soup.a) 
To get all <a>, use below code
print(soup.find_all(name = "a"))

print(soup.h1.text)

print(soup.find(name = "a").getText())
print(soup.find(name = "a").get("href"))

all_links = soup.find_all(name = "a")
for link in all_links:
    print(link.getText())
    print(link.get("href"))

print(soup.find(name = "h1", id="first-heading").getText())

first_heading = soup.find(class_ = "small-para")
print(first_heading.getText())

first_heading = soup.select(selector = "div .headings")
print(first_heading.getText())

first_heading = soup.select(selector = "#last-heading") 
print(first_heading.getText())


first_heading = soup.select(selector = ".last-para .headings")
print(first_heading.getText())