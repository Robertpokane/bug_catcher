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
    return render_template('bugs.html', bugs=mongo.db.bugs.find())
    
@app.route('/addbug')
def add_bug():
    return render_template('addbugs.html', projects=mongo.db.project.find())
    
@app.route('/addproject')
def add_project():
    return render_template('new_project.html')
    
@app.route('/projects')
def get_projects():
    return render_template('projects.html', projects=mongo.db.project.find())
    
@app.route('/insertbug', methods=["POST"])
def insertbug():
    bugs=mongo.db.bugs
    bugs.insert_one(request.form.to_dict())
    return redirect(url_for('get_bugs'))
    
@app.route('/edit_bug/<bug_id>')
def edit_bug(bug_id):
    the_bug =  mongo.db.bugs.find_one({"_id": ObjectId(bug_id)})
    projects =  mongo.db.project.find()
    return render_template('editbug.html', bug=the_bug, projects=projects)
    
@app.route('/editproject/<project_id>')
def editproject(project_id):
    project =  mongo.db.project.find_one({"_id": ObjectId(project_id)})
    return render_template('editproject.html', project=project)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)