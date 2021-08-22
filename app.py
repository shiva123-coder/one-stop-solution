import os
from flask import (
    Flask, render_template, flash,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
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
app.secret_key = os.environ.get("SERCET_KEY")

mongo = PyMongo(app)

# route to landing page
@app.route("/")
@app.route("/home")
def home():
    jobs = mongo.db.jobs.find()
    return render_template("home.html", jobs=jobs)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug=True)                              # Note : Debug value must be set to false once project completed


