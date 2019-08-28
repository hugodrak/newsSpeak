from gtts import gTTS
from bs4 import BeautifulSoup
import os, requests, sys, time
BASE_URl = "https://www.svd.se"

def getArticles(count):
	page = requests.get(BASE_URl)
	soup = BeautifulSoup(page.text, 'html.parser')
	articles = soup.find_all(class_='Teaser-link', href=True)
	links = []
	c = 0
	for a in articles:
		link = a['href']
		if c < count and link[:4] != "/om/":
			links.append(link)
		c+=1
	return links

def getPage(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	return(soup.find(class_='Deck').get_text())

def speak(text):
	tts = gTTS(text=text, lang='sv')
	tts.save("out.mp3")

	os.system("open out.mp3")
	time.sleep(15)

for link in getArticles(int(sys.argv[1])):
	speak(getPage(BASE_URl+link))
