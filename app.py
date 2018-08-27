import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
        
def checkredundant(thisname):
    _similar = mongo.db.recepies.find( { "recepie_name": thisname } )
    sim_list=[rec for rec in _similar]
    if not sim_list:
        return True
    else:
        return False

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb://admin:c9user@ds125402.mlab.com:25402/cook_book'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recepies')
def get_recepies():
    return render_template("recepies.html", 
    recepies=mongo.db.recepies.find())
    
@app.route('/get_recepies_ofcat/<category_name>')
def get_recepies_ofcat(category_name):
    myquery = { "category_name": category_name }
    recepies=mongo.db.recepies.find(myquery)
    this_list=[rec for rec in recepies]
    if not this_list:
        return '<h1 style="text-align:center; margin-top:5em;">Sorry there was no such recepies with this category, please go back</h1>'
    return render_template("recepiescat.html", 
    recepies=mongo.db.recepies.find(myquery), category_name=category_name)
    
@app.route('/get_recepies_ofdie/<diet_name>')
def get_recepies_ofdie(diet_name):
    myquery = { "diet_name":diet_name }
    recepies=mongo.db.recepies.find(myquery)
    this_list=[rec for rec in recepies]
    if not this_list:
        return '<h1 style="text-align:center; margin-top:5em;">Sorry there was no such recepies with this diet, please go back</h1>'
    return render_template("recepiesdiet.html", 
    recepies=mongo.db.recepies.find(myquery), diet_name=diet_name)
    
@app.route('/get_recepies_ofvote')
def get_recepies_ofvote():
    recepies=mongo.db.recepies.find().sort([("recepie_votes", -1)])
    return render_template("recepies.html", 
    recepies=recepies)

@app.route('/add_recepie')
def add_recepie():
    _categories=mongo.db.categories.find()
    _diets=mongo.db.diets.find()
    category_list=[category for category in _categories]
    diet_list=[diet for diet in _diets]
    return render_template('addrecepie.html', categories = category_list, diets = diet_list)
    
@app.route('/insert_recepie', methods=['POST'])
def insert_recepie():
    if checkredundant(request.form["recepie_name"]):
        recepies = mongo.db.recepies
        rec_dict = request.form.to_dict()
        del rec_dict["action"]
        rec_dict["recepie_votes"]=0
        recepies.insert_one(rec_dict)
        return redirect(url_for('get_recepies'))
    else:
        return '<h1 style="text-align:center; margin-top:5em;">Sorry there was a duplicate recepie in our system please go back</h1>'
    
@app.route('/edit_recepie/<recepie_id>') 
def edit_recepie(recepie_id):
    rec = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    all_categories = mongo.db.categories.find()
    all_diets = mongo.db.diets.find()
    return render_template('editrecepie.html', recepie=rec, categories=all_categories, diets=all_diets)
    
@app.route('/like_recepie/<recepie_id>') 
def like_recepie(recepie_id):
    recepies = mongo.db.recepies
    rec = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    current_vote = int(rec['recepie_votes'])
    current_vote +=1
    recepies.update( {'_id': ObjectId(recepie_id)},
    {
        'recepie_votes':current_vote,
        'recepie_name':rec['recepie_name'],
        'category_name':rec['category_name'],
        'recepie_ins':rec['recepie_ins'],
        'recepie_ingredients':rec['recepie_ingredients'],
        'diet_name':rec['diet_name'],
        'recepie_img':rec['recepie_img']
    })
    return redirect(url_for('get_recepies_ofvote'))

@app.route('/update_recepie/<recepie_id>', methods=["POST"])
def update_recepie(recepie_id):
    rec_dict = request.form.to_dict()
    rec = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    recepies = mongo.db.recepies
    recepies.update( {'_id': ObjectId(recepie_id)},
    {
        'recepie_votes': int(rec['recepie_votes']),
        'recepie_name':rec_dict['recepie_name'],
        'category_name':rec_dict['category_name'],
        'recepie_ins':rec_dict['recepie_ins'],
        'recepie_ingredients':rec_dict['recepie_ingredients'],
        'diet_name':rec_dict['diet_name'],
        'recepie_img':rec_dict['recepie_img']
    })
    return redirect(url_for('get_recepies'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
