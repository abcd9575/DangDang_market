import datetime
from flask_pymongo import PyMongo
from flask.json import jsonify
from flask import Flask, render_template, request, redirect # request는 요청하는 역할 redirect는 이동하는 역할

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app) 

@app.route('/detail')
def detail():
    product_db = mongo.db.product
    product = product_db.find_one({"title": request.args.get('title')})
    return jsonify({
        'title': product.get('title'),
        'content': product.get('content')
    })

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/write', methods = ["POST"])
def write():
    title = request.form.get('title')
    location = request.form.get('loc')
    price = request.form.get('price')
    content = request.form.get('content')

    mongo.db['product'].insert_one({
        "title": title,
        "price": price,
        "location": location,
        "content": content
    })
    return redirect('/') # 글을 쓰고나면 글을 쓴 곳을 다시 보여줘야하기 때문에 redirect 해줌.

@app.route('/')
def index():
    product_db = mongo.db.product
    products = product_db.find()
    return render_template('index.html',products=products)

if __name__ == '__main__':
    app.run()
