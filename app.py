import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'bug_catcher'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

#----------------Issues code------------------------------#
@app.route('/')
@app.route('/get_bugs')
def get_bugs():
    return render_template('bugs.html', bugs=mongo.db.bugs.find({'completed':{ '$ne':'on'}}))
    
@app.route('/addbug')
def add_bug():
    return render_template('addbugs.html', projects=mongo.db.project.find({'completed':{ '$ne':'on'}}))
    
@app.route('/edit_bug/<bug_id>')
def edit_bug(bug_id):
    the_bug =  mongo.db.bugs.find_one( {"_id": ObjectId(bug_id)})
    projects =  mongo.db.project.find( {'completed':{ '$ne':'on'}})
    return render_template('editbug.html', bug=the_bug, projects=projects)    
    
@app.route('/insertbug', methods=["POST"])
def insertbug():
    bugs=mongo.db.bugs
    bugs.insert_one(request.form.to_dict())
    return redirect(url_for('get_bugs'))
    
    
@app.route('/update_bug/<bug_id>', methods=["POST"])
def update_bug(bug_id):
    bugs = mongo.db.bugs
    bugs.update( {'_id': ObjectId(bug_id)},
    {
    'project_name':request.form.get('project_name'),
    'whats_wrong':request.form.get('whats_wrong'),
    'how_to_repeat': request.form.get('how_to_repeat'),
    'urgent':request.form.get('urgent'),
    'reoccuring':request.form.get('reoccuring')
    
    })
    
    return redirect(url_for('get_bugs')) 

@app.route('/delete_bug/<bug_id>')
def delete_bug(bug_id):
    mongo.db.bugs.remove({"_id": ObjectId(bug_id)})
    return redirect(url_for('get_bugs'))

@app.route('/remove_bug/<bug_id>')
def remove_bug(bug_id):
    mongo.db.bugs.remove({"_id": ObjectId(bug_id)})
    return redirect(url_for('get_complete'))    
    
@app.route('/complete_bug/<bug_id>')
def complete_bug(bug_id):
   the_bug =  mongo.db.bugs.find_one({"_id": ObjectId(bug_id)})
   projects =  mongo.db.project.find({'completed':{ '$ne':'on'}})
   return render_template('completebug.html', bug=the_bug, projects=projects)
   
@app.route('/migrate_bug/<bug_id>', methods=["POST"])
def migrate_bug(bug_id):
    bugs = mongo.db.bugs
    bugs.update( {'_id': ObjectId(bug_id)},
    {
    'project_name':request.form.get('name'),
    'whats_wrong':request.form.get('whats_wrong'),
    'how_to_repeat': request.form.get('how_to_repeat'),
    'urgent':request.form.get('urgent'),
    'reoccuring':request.form.get('reoccuring'),
    'fix':request.form.get('fix'),
    'completed':request.form.get('completed')
    })
    return redirect(url_for('get_complete', bug=bugs))  

#----------------Projects code------------------------------#

@app.route('/addproject')
def add_project():
    return render_template('new_project.html')
    
@app.route('/projects')
def get_projects():
    return render_template('projects.html', projects=mongo.db.project.find({'completed':{ '$ne':'on'}}))

@app.route('/editproject/<project_id>')
def editproject(project_id):
    project =  mongo.db.project.find_one( {"_id": ObjectId(project_id)})
    return render_template('editproject.html', project=project)

@app.route('/delete_project/<project_id>')
def delete_project(project_id):
    mongo.db.project.remove({"_id": ObjectId(project_id)})
    return redirect(url_for('get_projects'))


@app.route('/update_project/<project_id>', methods=["POST"]) 
def update_project(project_id):
   
    project = mongo.db.project
    project.update( {'_id': ObjectId(project_id)},
    {
      'name':request.form.get('name'),
      'description':request.form.get('description'),
      'com_date':request.form.get('com_date')
      
    })
    print(request.form)
    return redirect(url_for('get_projects'))

@app.route('/insertproject', methods=["POST"])
def insertproject():
    project=mongo.db.project
    project.insert_one(request.form.to_dict())
    return redirect(url_for('get_projects'))

    
@app.route('/complete_project/<project_id>')
def complete_project(project_id):
   projects =  mongo.db.project.find_one({"_id": ObjectId(project_id)})
   return render_template('completedproject.html', project=projects)

@app.route('/get_complete')
def get_complete():
    return render_template('completedlist.html', bugs=mongo.db.bugs.find({'completed':'on'}))

@app.route('/end_project/<project_id>', methods=["POST"])
def end_project(project_id):
    
    project = mongo.db.project
    project.update( {'_id': ObjectId(project_id)},
    {
   'name':request.form.get('name'),     
   'description':request.form.get('description'),
   'com_date':request.form.get('com_date'),
   'completed':request.form.get('completed'),
   'com_date_actual':request.form.get('com_date_actual'),
   'delay-reason':request.form.get('delay')
    })
    
    return redirect(url_for('get_projects', projects=project))    

   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)