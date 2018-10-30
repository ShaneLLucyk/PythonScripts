#Import Libraries
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/title/tt1270797/?ref_=fn_al_tt_1')
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
print(soup.prettify())
print(soup.prettify())
