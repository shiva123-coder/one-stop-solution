import os
from flask import (
    Flask, render_template, flash,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

"""
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "cZr6kfUiN7")
os.environ.setdefault("MONGO_URI", "mongodb+srv://shiva:Gitclub123@myfirstcluster.9kpcw.mongodb.net/services?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "services")

"""

# create an instance of flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# route to landing page
@app.route("/")
@app.route("/home")
def home():
    jobs = mongo.db.jobs.find()
    return render_template("home.html", jobs=jobs)


# route to login page
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
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# route to register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username is already exits in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exits")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug=True)                              # Note : Debug value must be set to false once project completed


