import os
import re
from flask import (
    Flask, render_template, flash,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# create an instance of flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# home page
@app.route("/")
@app.route("/home")
def home():
    jobs = mongo.db.jobs.find()
    return render_template("home.html", jobs=jobs)


# search functionality
"""
code taken from walkthrough project of CI
and modified as per project requirement
--start--
"""
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    jobs = list(mongo.db.jobs.find({"$text": {"$search": query}}))
    return render_template("home.html", jobs=jobs)
"""
code taken from walkthrough project of CI
and modified as per project requirement
--End--
"""


# user login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username is already exits in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("account", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username is already exits in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash(
                f"username {request.form.get('username')} is alraedy registered\
                     please try different username")
            return redirect(url_for("register"))
        
        """
        check length of username is within the limit and
        display flash message if length is outside of its limit
        and redirect user to registration page again
        """
        if len(request.form.get("username")) not in range(5, 13):
            flash (
                "username should be between 5-12 character, please try again")
            return redirect(url_for("register"))

        """
        check length of password is within the limit and
        display flash message if password length is outside of its limit
        and redirect user to registration page again

        """
        if len(request.form.get("password")) not in range(5, 13):
            flash(
                "password should be between 5-12 character, please try again")
            return redirect(url_for("register"))
        
        # check if password contain any space
        password_supplied = request.form.get("password")
        if ' ' in password_supplied:
            flash("Password should contain no space")
            return redirect(url_for("register"))

        """
        check wether password contain atleast one
        special character or not and display flash
        message accordingly.

        concept of validating special character was taken from youtube
        video of SDTE- Automatopn Techie (
        https://www.youtube.com/watch?v=mG3aGgFYJSE)

        """
        password_supplied = request.form.get("password")
        char = re.compile('[@_!#$%^&£()<>?|/\}{¬;*"=+]')
        if(char.search(password_supplied) == None):
            flash("password should contain atleast one special character")
        else:
            flash(" Registration Successful!")
        return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for(
            "account", username=session["user"]))
    return render_template("register.html")


# user profile page
@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    if "user" in session:
        current_user = mongo.db.users.find_one({"_id": ObjectId()})
        job_creator = mongo.db.jobs.find_one({"added_by": "user"})
        if current_user == job_creator:
            # retreive only username from database
            username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]

            # retrive job details created by user
            services = list(mongo.db.jobs.find(
                {"added_by": session["user"]}))   

    
            return render_template(
                "account.html", username=username, services=services)
        else:
            flash("You are not authorised to view this page")
            return redirect(url_for("login"))
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add new job to the page
@app.route("/add_job", methods=["GET", "POST"])
def add_job():
    if "user" in session:
        current_user = mongo.db.users.find_one({"_id": ObjectId()})
        job_creator = mongo.db.jobs.find_one({"added_by": "user"})
        if current_user == job_creator:
            if request.method == "POST":
                job = {
                    "img_url": request.form.get("img_url"),
                    "job_type": request.form.get("job_type"),
                    "company_name": request.form.get("company_name"),
                    "cost": request.form.get("cost"),
                    "phone": request.form.get("phone"),
                    "email": request.form.get("email"),
                    "desc": request.form.get("desc"),
                    "added_by": session["user"]
                }
                mongo.db.jobs.insert_one(job)
                flash("Job successfully added")
                return redirect(url_for("home"))
        else:
            flash("You are not authorised to add new job")
            return redirect(url_for("login"))

        selections = mongo.db.jobs.find()
        return render_template("add_job.html", selections=selections)
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for("login"))


# edit job
@app.route("/edit_job/<job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    if "user" in session:
        current_user = mongo.db.users.find_one({"_id": ObjectId()})
        job_creator = mongo.db.jobs.find_one({"added_by": "user"})
        if current_user == job_creator:
            if request.method == "POST":
                send = {
                    "img_url": request.form.get("img_url"),
                    "job_type": request.form.get("job_type"),
                    "company_name": request.form.get("company_name"),
                    "cost": request.form.get("cost"),
                    "phone": request.form.get("phone"),
                    "email": request.form.get("email"),
                    "desc": request.form.get("desc"),
                    "added_by": session["user"]
                }
                mongo.db.jobs.update({"_id": ObjectId(job_id)}, send)
                flash("Job successfully updated")
                return redirect(url_for('account', username=session['user']))
        
            job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
            selections = mongo.db.jobs.find()
            return render_template("edit_job.html", job=job, selections=selections)

        else:
            flash("You are not authorised to edit this job")
            return redirect(url_for("login"))
    else:
            flash("You must be logged in to view this page")
            return redirect(url_for("login"))
    
    

# user to delete their job from page
# user can only delete their own job
@app.route("/delete_job/<job_id>")
def delete_job(job_id):
    if "user" in session:
        current_user = mongo.db.users.find_one({"_id": ObjectId()})
        job_creator = mongo.db.jobs.find_one({"added_by": "user"})
        if current_user == job_creator:
            mongo.db.jobs.remove({"_id": ObjectId(job_id)})
            flash("Delete request has now Completed")
            return redirect(url_for('account', username=session['user']))
        else:
            flash("You are not authorise to perform this action")
            return redirect(url_for("login"))
    else:
        flash("You must be logged in to view this page")
        return redirect(url_for("login"))


# admin to delete job from the page
# admin can delete job that added by any user too
@app.route("/delete_job_by_admin/<job_id>")
def delete_job_by_admin(job_id):
    if "user" in session :
        # main_user = mongo.db.users.find_one({"_id": ObjectId()})
        # admin_user = mongo.db.jobs.find_one({"added_by": "admin"})
        # if main_user == admin_user:
            mongo.db.jobs.remove({"_id": ObjectId(job_id)})
            flash("Delete request has now Completed")
            return redirect(url_for('admin'))
    else:
        flash("You are not authorise to perform this action")
        return redirect(url_for("login"))
    

# admin access only
@app.route("/admin")
def admin():
    all_jobs = mongo.db.jobs.find()
    return render_template("admin.html", jobs=all_jobs)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug=True)                              # Note : Debug value must be set to false once project completed


