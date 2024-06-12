from flask import Blueprint, request, jsonify, redirect, url_for, Response

import json
from .utils import *


views = Blueprint("views", __name__)



@views.route("/<cn>")
def get_party_cn(cn):

    # seding CN Number and fetch data from database matching data
    """
        request:
            http://127.0.0.1:5000/6010538553
        response:
                [["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5034588, "TWINRAB 1500IU/2.5ML
                INJ. VIAL SL DOM", "1 VIAL", "B200041", "01.01.2024", "Expiry", 1, 2221, null, null, null, null, null, "ZLL-1", null,
                null, null, null], ["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5034591,
                "TWINRAB 600IU/1ML INJECTION VIAL SL DOM", "1VIAL", "B200026", "01.01.2024", "Expiry", 2, 2444, null, null, null, null,
                null, "ZLL-1", null, null, null, null], ["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870",
                "03.02.2024", 5023878, "VACTYPH INJECTION 10X1X0.5ML SALE DOM", "10X1X0.5 ML", "05FS12B", "01.10.2023", "Expiry", 21,
                1103, null, null, null, null, null, "ZLL-1", null, null, null, null], ["565", "91", "AVADH MEDICINES", "LUCKNOW",
                "6010538553", "1496124870", "03.02.2024", 5041829, "Vaxiflu-4 Inj St 2023SH 0.5ml PFS Sl Dom", "1X 0.5ML PFS",
                "04HP08B", "01.02.2024", "Expiry", 10, 6825, null, null, null, null, null, "ZLL-1", null, null, null, null], ["565",
                "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5009399, "VAXIRAB -N INJ. SALE DOM 1COMBI
                PACK", "1COMBI PACK", "RV10009", "01.12.2023", "Expiry", 1, 0, null, null, null, null, null, "ZLL-1", null, null, null,
                null], ["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5009399, "VAXIRAB -N INJ.
                SALE DOM 1COMBI PACK", "1COMBI PACK", "RV10012", "01.12.2023", "Expiry", 2, 494, null, null, null, null, null, "ZLL-1",
                null, null, null, null], ["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5041211,
                "ZYVAC MMR INJ 1X0.5ML VIAL COMBIPACK DO", "0.5ML VIAL COMBIPA", "07FS02C", "01.12.2023", "Expiry", 5, 1465, null, null,
                null, null, null, "ZLL-1", null, null, null, null], ["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553",
                "1496124870", "03.02.2024", 5041211, "ZYVAC MMR INJ 1X0.5ML VIAL COMBIPACK DO", "0.5ML VIAL COMBIPA", "07FS03C",
                "01.12.2023", "Expiry", 2, 525, null, null, null, null, null, "ZLL-1", null, null, null, null], ["565", "91", "AVADH
                MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5029191, "ZYVAC TCV INJECTION 1X0.5 ML PFS SL DOM",
                "1X0.5ML PFS", "06FP24B", "01.12.2023", "Expiry", 1, 727, null, null, null, null, null, "ZLL-1", null, null, null,
                null]]
    """
    result = get_cn(cn)

    response = Response(response=json.dumps(result))
    return response




@views.route("/user_info", methods=["POST"])
def get_party_info():
    """
    request:
        {
            "plt":565,
            "comman_cn":6010538553,
            "batch_no":"'B200041'"
        }
    response:
        ["565", "91", "AVADH MEDICINES", "LUCKNOW", "6010538553", "1496124870", "03.02.2024", 5034588, "TWINRAB 1500IU/2.5ML
        INJ. VIAL SL DOM", "1 VIAL", "B200041", "01.01.2024", "Expiry", 1, 2221, null, null, null, null, null, "ZLL-1", null,
        null, null, null]      
    """
    data = json.loads(request.data)
    result = party_infomation(data)
    response = Response(response=json.dumps(result))
    return response

