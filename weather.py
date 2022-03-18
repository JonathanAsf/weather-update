#unfinished
import requests 
from bs4 import BeautifulSoup

search="Clima em São Palo"

url=f"https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp"

r=requeust.get(url)
s=BeautifulSop(r.text,"html.parser")

update=s.find("div",class_="BNeawe").text
print(update)
