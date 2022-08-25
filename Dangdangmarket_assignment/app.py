import math
from flask import Flask, request, redirect, render_template
from flask_pymongo import PyMongo
from flask.json import jsonify

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)


@app.route('/detail')
def detail():
    products = mongo.db.product
    result = products.find_one({"title": request.args.get('title')})
    
    return jsonify({
        "title": result.get('title'),
        "content": result.get('content')
    })

@app.route('/')
def index():
    products = mongo.db.product
    page = int(request.args.get('page',1))
    limit = 3
    skip = limit * (page - 1)
    count = mongo.db['product'].count_documents({})
    max_page = math.ceil(count / limit)

    pages = range(1, max_page +1)
    merchandise = mongo.db['product'].find().limit(limit).skip(skip)
    
    byunsoo = products.find().limit(limit).skip(skip)
    return render_template('index.html', products = byunsoo, pages=pages)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/write', methods=["POST"]) 
def write():
    products = mongo.db.product
    products.insert_one({
        "title": request.form.get('title'),
        "price": request.form.get('price'),
        "location": request.form.get('loc'),
        "content": request.form.get('content')
    })
    return redirect('/')


if __name__ == '__main__':
    app.run()
    