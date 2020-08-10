import os
from flask import Flask, render_tempplate, redirect, request, url_for
from flask_pymongo import PyMongo

# creates an instance of flask and assign it to the app variable
app = Flask(__name__)

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "meet_event"
COLLECTION_NAME = "theFirstDB"
SECRET_KEY = os.environ.get('SECRET_KEY')