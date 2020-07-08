# Importieren der Bibliotheken
import requests
from bs4 import BeautifulSoup

# Initialisierung
subsI = []
subsYT = []

# Einlesen der Webseiten
while len(subsI) == 0:
    insta = requests.get('https://www.instagram.com/official.offtheroad/?hl=de')
    soupI = BeautifulSoup(insta.text, 'html.parser')
    subsI = soupI.find_all('meta', property="og:description")
while len(subsYT) == 0:
    youtube = requests.get('https://www.youtube.com/channel/UCw8GywizCke8mo0RRZL_0bg')
    soupYT = BeautifulSoup(youtube.text, 'html.parser')
    subsYT = soupYT.find_all('span', {"class": "yt-subscription-button-subscriber-count-branded-horizontal"})

# Formatierung
subcountI = str(subsI)[16:].split()[0]
subcountYT = str(subsYT)[19:].split()[0]

# Ausgabe
print('Aktuelle Instagram Abonnenten:', subcountI)
print('Aktuelle Youtube Abonnenten:', subcountYT)
