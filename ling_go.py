import json
import requests
import bs4 as BeautifulSoup
import time


with open("./data.json", 'r') as f:
    data = json.load(f)

for d in data:
    inpt = input("Next!")
    if inpt == "n":
        break
    else:
        print(d)