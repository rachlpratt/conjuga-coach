from flask import Flask, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return "Home page"
