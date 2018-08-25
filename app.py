import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb://admin:c9user@ds125402.mlab.com:25402/cook_book'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recepies')
def get_recepies():
    return render_template("recepies.html", 
    recepies=mongo.db.recepies.find())

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        