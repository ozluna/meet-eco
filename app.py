import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env  # noqa: F401


# creates an instance of flask and assign it to the app variable
app = Flask(__name__)


# connecting DB to the app
app.config["MONGO_DBNAME"] = 'meet_event'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    ca = list(mongo.db.event_categories.find())
    the_event = list(mongo.db.events.find())
    return render_template("index.html", events=the_event, event_categories=ca)


@app.route("/create_event")
def create_event():
    event_cat = mongo.db.event_categories.find()
    return render_template("createevent.html", event_categories=event_cat)


@app.route("/insert_event", methods=["POST"])
def insert_event():
    mongo.db.events.insert_one(request.form.to_dict())
    return redirect(url_for('created_event'))


@app.route("/edit_event/<event_id>", methods=['POST'])
def edit_event(event_id):
    id_no = request.form.get('id_no')
    print(event_id)
    print(id_no)
    if id_no == event_id:
        events = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        cats = mongo.db.event_categories.find()
        return render_template("editevent.html",
                               event=events, event_categories=cats
                               )


@app.route('/update_event/<event_id>', methods=['POST'])
def update_event(event_id):
    event = mongo.db.events
    event.update({'_id': ObjectId(event_id)},
                 {
        'event_name': request.form.get('event_name'),
        'event_description': request.form.get('event_description'),
        'event_date': request.form.get('event_date'),
        'places': request.form.get('places'),
        'event_pic': request.form.get('event_pic')
    })
    return redirect(url_for('index'))


@app.route('/remove_event/<event_id>')
def remove_event(event_id):
    mongo.db.events.remove({'_id': ObjectId(event_id)})
    return redirect(url_for('index'))


@app.route('/insert_attender/<event_id>', methods=['POST'])
def insert_attender(event_id):
    event = mongo.db.events
    event.update({'_id': ObjectId(event_id)},
                 {'$addToSet': {
                    "guests": {
                        'fname': request.form.get('fname'),
                        'lname': request.form.get('lname'),
                        'email': request.form.get('email')
                    }
                 }})
    return redirect(url_for('index'))


# grap the id number and print to the screen for the creator so they
#  can do edit and delete
@app.route('/created_event')
def created_event():
    the_event = mongo.db.events.find({}).sort([('_id', -1)]).limit(1)
    for event in the_event:
        eventId = event["_id"]
        organiser = event["organiser_name"]
        return render_template('createdevent.html', eventId=eventId,
                               organiser=organiser)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

