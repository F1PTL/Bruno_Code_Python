from bs4 import BeautifulSoup
import urllib.request
import lxml

# récupérer le html de la page en question en faisant un appel http
html = urllib.request.urlopen("https://www.commitstrip.com/fr/")

# convertir avec la librairie beautifulSoup
soup = BeautifulSoup(html, features="lxml")

# soup possède des méthode
# select_one(selector) -> ramène un élément qui correspond au selector
# select(selector)  -> ramène la liste des élèments qui correspond au selector

lien = soup.select_one("div.excerpt section a")

# récupérer le html de la page en question en faisant un appel http
htmlfinal = urllib.request.urlopen(lien.get("href"))

# convertir avec la librairie beautifulSoup
soupfinal = BeautifulSoup(htmlfinal, features="lxml")

selectorTime = 'div.entry-meta a time'
selectorImg = 'div.entry-content p img'

date = soupfinal.select_one(selectorTime)
print(date.get_text())

image = soupfinal.select_one(selectorImg)
print(image.get('src'))