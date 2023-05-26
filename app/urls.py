from app import app
from .views import *


@app.route('/')
def index():
    return Index()

@app.route("/new/", methods=['GET','POST'])
def new_quiz():
    return NewQuiz()

@app.route("/get/")
def get_quiz():
    return GetQuiz()

@app.route("/get/query=<query>")
def get_single_quiz(query):
    return GetQuiz(query)
