
import json
from flask import Blueprint, request, jsonify, redirect, url_for
from .utils import *


views = Blueprint("views", __name__)


@views.route("/", methods=["POST"])
def hello_world():

    """
        request:
            dat_frame: master_file_name
        response:
            data is inserted
    """
    data = request.files['data_frame']
    return create_table_insert_recode(data)

