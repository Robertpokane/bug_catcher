import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'bug_catcher'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bugs')
def get_bugs():
    return render_template("bugs.html", bugs=mongo.db.bugs.find())
    
@app.route('/addbug')
def add_bug():
    return render_template('addbugs.html', projects=mongo.db.project.find())
    
@app.route('/addproject')
def add_project():
    return render_template('new_project.html')
    
@app.route('/projects')
def get_projects():
    return render_template("projects.html", projects=mongo.db.project.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)