from flask import Blueprint, request, jsonify, redirect, url_for
import json
from .utils import *


views = Blueprint("views", __name__)



@views.route("/")
def hello_world():
    return "Hello, World!"


