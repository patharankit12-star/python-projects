import requests

from bs4 import BeautifulSoup
# find html fronted page 
url = "https://www.amazon.com"
response = requests.get("http://www.amazon.com")
print(response.text)

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

for handing in soup.find_all("Amazon"):
    print(heading.text)

'''url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":'foo',
    "body":'bar',
    "userid":1,
}

headers = {
    'Content-type' : 'application/json; charset=UTF-8',
}
response=requests.post(url,headers=headers,json=data)'''