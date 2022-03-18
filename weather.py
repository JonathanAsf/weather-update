import requests
import json

cidade = input("Escreva a sua cidade")

requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=941329145b3169e765ace5e77ff936d4')
                     
print(requisicao.text)


#Some cities cannot be found
