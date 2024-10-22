from flask import Blueprint
from datetime import datetime

home_resource = Blueprint('home', __name__)

@home_resource.route("/")
def home():
    date = str(datetime.now())
    print(date)
    return {"Data do servidor": date}