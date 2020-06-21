Issue Tracker
For this Milestone project I took inspiration from Googles toothbrush test. “If you run into a problem as much as you use your toothbrush then you must find a way to change it”. I applied that idea to my projects and noticed that I was spending too long flicking through pages of notes to find some of the issues or changes that I wanted to make to any project. Some had been completed, some scraped some taken down multiple times. So I decided I needed to make myself an ISSUE TRACKER.
UX
So I set out to design a project that would fit my needs. A CRUD application that is hosted online with a simplistic design and easy to use interface to hold all my thoughts, design ideas, issues that I could not amend right away. 
Some of Items that I had in in mind that I came across while going through the Tracker:
•	Some of the branding was incorrect ie calling it “new bug” in one page, “edit issue” in another page, and calling them “problems” on a different page. I opted for” “issue” as this was primarily for the tracking of issues not just ideas for the project
•	I didn’t want the tracker to be very flashy or “in your face” I had considered using animated icons and pulsing buttons but that would of just been distracting. The purpose of those is to draw the user’s eye/ attention to what ever the owner needs the user to look at, like say a deal on a product or to the check out in a shopping site. They would have been nice to have but not appropriate for the Project.
I had a vision of how I wanted my site to look and stuck as closely to that as I could. The wireframes that I have used can be found here. Or alternatively they can be found at my github - https://github.com/Robertpokane/bug_catcher/tree/master/Wireframes

Features
This is a Full CRUD project that you can create read update and delete both issues as well as the projects that they are attached to.

Existing Features
•	Feature 1 - allows users to create a new project complete with description and due date
•	Feature 2 - allows users to update that all 3 fields of that project
•	Feature 3 - allows users to delete that project if it is made in error
•	Feature 4 - allows users to mark each created project as complete.
•	Feature 5 - allows users to view all projects and filters out all projects that are marked as complete
•	Feature 6 - allows users to create a new issue asking what is going wrong, how to repeat the error assign it to a project (drop down list filtered all completed projects out)
•	Feature 7 - allows users to update that all fields of that issue
•	Feature 8 - allows users to delete that issue if it is made in error
•	Feature 9 - allows users to mark each created issue as complete.
•	Feature 10 - allows users to view all completed issue and delete if necessary
In my app.py I have used a particularly useful piece of code within my find function if I needed to filter out any completed (or in some other cases completed projects or issues)  mongo.db.project.find({'completed':{ '$ne':'on'}}))

Features Left to Implement
•	What I can update is to set up more filters on the home page to have each project separated into their own section with their own list of issues
•	Set up an ideas section, instead of this being just an issue tracker I can add a drop down in the create new issue section (renaming it ne entry) for Issues/ Ideas and send the entry to a particular collection based on that to make an all purpose tracker.  
•	Amalgamate the 3 forms (new Ideas/Issues /Projects into one button have that take the user to another selection screen or use the dropdowns to open/close accordion elements and disable the others from use  
•	Cross reference feature so that if there has been a repeating issue that it can be linked to another _id number

Technologies Used
This is a list of all the languages, frameworks, libraries, and any other tools that I have used to construct this project.
•	JQuery
o	The project uses JQuery to make the materialize functions work correctly IE accordion options on home screen or the calendar from the create project menu.
•	HTML
o	Used a to display all the elements in the correct manner on the site 
•	CSS
o	Used to colour and set the elements apart from each other in the site
•	Pyhton
o	Used as the primary language to tell what buttons to do which functions, what each of those functions actually do and what is passed between mongo and my site
•	Jinja
o	Used this templating language in python which keeps the size of the overall site down and speeds up development overall
•	Materialze
o	Used their components as they are simple, easy to use and make the site look as beautiful as it can with as much functionality as I need.
•	Material-Icons
o	Used for the icons before all elements of my forms
•	Flask 
o	Used as a simple way to talk to my SQL database
o	Render_template is used to “refresh” the data that is displayed on the site from the date base IE after an entry has went through a CRUD operation
o	Redirect used after an operation to another function IE after an entry is created and the save button is clicked the code will redirect the “get_bugs” function where it will reload the home page with the new entry displaying
o	url_for is used in conjunction with redirect to reload a web page. It is also used in all my navigation elements
•	BSON.ObjectId
o	Is used to identify MONGO DB objects their _Id number
•	Pymongo
o	This was used as a toll for my code to easily talk to mongodb
•	Flask-Pymongo
o	Flask-PyMongo bridges Flask and PyMongo
•	MongoDB
o	Used to store and retrieve all my data used for this project

Testing
As this project is not as big as some of my previous attempts I have continually tested as I went along fixing minor issues as they cropped up and after my project has been deployed to Heroku I preformed a full CRUD operation on both new and previously existing Issues and projects that I have logged. 
Because of the consistent testing there have been no serious issues that had not been addressed and fixed. But inevitability there had been  a few issues that I had over looked during the initial development process.
Repaired Issues/Completed Projects
•	Both “How the error was amend” section and “What, if any, was the delay in completion” sections where slightly out of line due to not having Material Icons at their sides.

Edit Project
•	Edit project “Project Finish date” section would not amend to any date than it was initially set up with then during attempting to fix it, the date assigned to each entry would not show up at all on the site. My initial attempt to repair the issue was mistaken. I had thought that the jquery was incorrect used to display the feature so I removed editing it all together and noticed that nothing could be edited in “Edit projects. That lead me to the correct error. In my Python code for update_project I had a capital D in the id of project.update( {'_id': ObjectId(project_id)}, which needless to say, threw the whole thing off. Once I replaced the elements and jquery I removed and fixed the _id it worked perfectly

Mobile navigation
•	The only issue with the mobile navigation is that I missed “New Problem” when rebranding my project Interface to “Issue”

Other that the issues above I created 2 new Test projects, and 2 New test issues. I assigned one of the pre-existing projects to one of the new issues and one of the new projects to the new issues. I named one issue “complete me” and the other “delete me” and did the same for the projects. I edited the “complete me” Issue to change the project it was assigned to placed a number after both the “What Is The Error?” and “How To Repeat The Error” sections and all worked so Marked it as repaired which took me to the “Repaired issues”  and clicked delete on the screen for it to be removed. That tested all the functions of the Issues section  which came back with no issues. I then went to the home page and deleted the issue “delete me”, that worked with no issues and then preformed the same tests with the projects known as complete me” and “delete me” editing all and deleting them as before with no issues with the sections

Deployment
The process of deploying my code to Heroku was a fairly simple one, the beginning on of my project I created a GitHub and a Heroku repo after logging into both through the CLI in AWS Cloud9 I just had to keep up with the commits and git push’s to each Repo through out. After my final commit I pushed the code to my Heroku and input the MONGO_DBNAME and  MONGO_URI Config Vars into Heroku and then I had Heroku talking to my MongoDB using Python for a fully functional Application at 
http://bug-catcher-flask.herokuapp.com/	
and the code for my project is on Github at – 
https://github.com/Robertpokane/bug_catcher 

Credits

Media
•	The form elements, navigation elements and relating Jquery was taken from Materialize - https://materializecss.com/ 
Acknowledgements
•	I received help with the deployment of my project from Tutor Sammy in the code institute – I had far too many modules in my Requirements.txt file. She helped me whittle them down to the ones that my project was actually using and explained the config vars to me so that my project could be properly deployed.

