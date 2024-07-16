
import json
from flask import Blueprint, request, jsonify, redirect, url_for
from .utils import *


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    return "home page"

@views.route("/master", methods=["POST"])
def upload_master_file():
    """
    request:
        data_frame: master_file_name
    response:
        data is inserted
    """
    
    master_file = request.files['data_frame']
    location = request.form.get('location')
    
    print(location)
    
    return create_table_insert_recode(master_file, location)
