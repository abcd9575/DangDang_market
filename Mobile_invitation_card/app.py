import math
import datetime
import imp
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect # request는 요청하는 역할 redirect는 이동하는 역할

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/write', methods = ["POST"])
def write():
    name = request.form.get('name')
    content = request.form.get('content')

    mongo.db['wedding'].insert_one({
        "name": name,
        "content": content
    })
    return redirect('/') # 글을 쓰고나면 글을 쓴 곳을 다시 보여줘야하기 때문에 redirect 해줌.

@app.route('/')
def index():
    now = datetime.datetime.now()
    wedding = datetime.datetime(2022, 8, 14, 0, 0, 0)
    diff = (wedding -now).days
    if diff <= 0:
        diff = "DAY"
    

    count = mongo.db['wedding'].count_documents({})
    limit = 3
    page = int(request.args.get('page',1))
    skip = limit*(page-1)

    max_page = math.ceil(count/limit)

    pages = range(1,max_page+1)
    
    
    guestbooks = mongo.db['wedding'].find().limit(limit).skip(skip)
    return render_template('index.html',
        days=diff,
        guestbooks=guestbooks,
        pages = pages
    )

if __name__ == '__main__':
    app.run()
