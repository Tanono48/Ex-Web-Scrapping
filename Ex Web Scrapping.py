import requests
from bs4 import BeautifulSoup

url ="https://www.newbalance.com/men/shoes/lifestyle/"
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text, 'html.parser')
find_word = soup.find_all("span",{"class":"category-name font-body w-100 d-block pt-2"})

for i in find_word:
  print(i)
