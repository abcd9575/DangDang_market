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
    byunsoo = products.find()
    return render_template('index.html', products = byunsoo)


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
    