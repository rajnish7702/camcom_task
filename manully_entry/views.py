
import json
from flask import Blueprint, request
from .utils import *


views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
    return "home page"


@views.route("/manully_update", methods=["POST"])
def manully_views():
    """
        request:
            {
                "comman_cn": "'5196950696'",
                "batch_no": "'I201727'"
            }
            dat_frame: master_file_name
        response:
            data is inserted
    """
    print("!"*50)
    data = json.loads(request.data)
    return update_reports(data)


@views.route('/add_items', methods=["POST"])
def addItems():

    data = json.loads(request.data)

    pass
