import requests

# from bs4 import BeautifulSoup


# Making a GET request
r = requests.get("http://yodi.my.id")

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
print(r.content)
