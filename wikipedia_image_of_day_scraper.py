import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day"

response = requests.get(url)

# Get Image
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
image = soup.find("img")
print( image["src"] )

# Get Image #2
soup = BeautifulSoup(response.content, "html.parser")
anchor = soup.find("a", {"class":"image"} )
print( anchor.img["src"] )

# Get Text
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("div", {"id":"mp-tfp"} )
print( table.p.text )

# Get Link
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("div", {"id":"mp-tfp"} )
print( "https://en.wikipedia.org/" + table.p.a["href"] )

# get all pictures of day for a month:
url = "https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day/January_2020"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all("table", {"role":"presentation"} )

for table in tables:
    print( table.img["alt"], "," , table.img["src"][2:], "\n")

