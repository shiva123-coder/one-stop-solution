import os
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


# create an instance of flask

app = Flask(__name__)

app.secret_key = "super secret key"

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secter_key = os.environ.get("SERCET_KEY")

mongo = PyMongo(app)


@app.route("/")
def hello():
    return "This is initial test only"
    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug=True)                              # Note : Debug value must be set to false once project completed


