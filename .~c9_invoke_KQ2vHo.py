import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb://admin:c9user@ds125402.mlab.com:25402/cook_book'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recepies')
def get_recepies():
    return render_template("recepies.html", 
    recepies=mongo.db.recepies.find())

@app.route('/add_recepie')
def add_recepie():
    _categories=mongo.db.categories.find()
    _diets=mongo.db.diets.find()
    category_list=[category for category in _categories]
    diet_list=[diet for diet in _diets]
    return render_template('addrecepie.html', categories = category_list, diets = diet_list)
    
@app.route('/insert_recepie', methods=['POST'])
def insert_recepie():
    thisname = request.form["recepie_name"]
    _similar = mongo.db.recepies.find( { "recepie_name": thisname } )
    sim_list=[rec for rec in _similar]
    if not sim_list:
        recepies = mongo.db.recepies
        rec_dict = request.form.to_dict()
        del rec_dict["action"]
        rec_dict["recepie_votes"]=0
        recepies.insert_one(rec_dict)
        return redirect(url_for('get_recepies'))
    else:
        return 'Sorry there was a duplicate recepie in our system please go back'
    
@app.route('/edit_recepie/<recepie_id>') 
def edit_recepie(recepie_id):
    rec = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    all_categories = mongo.db.categories.find()
    all_diets = mongo.db.diets.find()
    return render_template('editrecepie.html', recepie=rec, categories=all_categories, diets=all_diets)

@app.route('/update_recepie/<recepie_id>', method=["POST"])
def update_recepie(recepie_id):
    recepies = mongo.db.recepies
    recepies.update( {'_id': ObjectId(r)} )

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        