import datetime
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect # request는 요청하는 역할 redirect는 이동하는 역할

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
@app.route('/register')
def register():
    return render_template('register.html')
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
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
