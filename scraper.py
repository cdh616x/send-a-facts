from bs4 import BeautifulSoup
import requests
import random

url = "https://www.keepinspiring.me/famous-quotes/"
response = requests.get(url)
print(response)

quotes = []

soup = BeautifulSoup(response.text, "html.parser")
raw = (soup.find_all(name="blockquote", class_="wp-block-quote"))
for n in raw:
    text = n.getText()
    replaced_text = text.replace(".", " - ")
    quotes.append(replaced_text)

random_quote = (random.choice(quotes))