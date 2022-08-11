# import requests
# from bs4 import BeautifulSoup

# res = requests.get("http://www.yes24.com/24/Category/BestSeller")
# soup = BeautifulSoup(res.text,"html.parser")

#     ts = soup.select_one("#bestList > ol > li.num"+ idx +" > p:nth-child(3) > a")
#     print(ts.text)

import requests
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.local

collection = db.yes24

rows = collection.find()
for row in rows:
    print(row)

res = requests.get("http://www.yes24.com/24/Category/BestSeller")
soup = BeautifulSoup(res.text, "html.parser")
# print(res.text)
# print(soup)
for i in range(40):
    idx = str(i+1)
    if idx == "19": 
        idx = "19_line"
    elif idx == "20":
        idx = "20_line"
    title = soup.select_one(f"#bestList > ol > li.num{idx} > p:nth-child(3) > a")


    db['yes24'].insert_one({
         'Title': title.text
    })


























