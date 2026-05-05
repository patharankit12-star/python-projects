import requests
import json

query =input("which type of news you shows?:")

API_KEY = "54c5925fced2454ebd7ae4c8266fd773"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-03-20&sortBy=publishedAt&apiKey={API_KEY}"

r = requests.get(url)
news = json.loads(r.text)

#print(news,type(news))

for article in news["articles"]:
    # selected news title and discription print only
    print(article["title"])
    print(article["description"])
    print("----End of this news -----")