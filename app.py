import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


# creates an instance of flask and assign it to the app variable
app = Flask(__name__)


# connecting DB to the app
app.config["MONGO_DBNAME"] = 'meet_event'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", events=mongo.db.events.find())


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

