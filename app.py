import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# create an instance of flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is initial test only"
    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug=True)                              # Note : Debug value must be set to false once project completed


