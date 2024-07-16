from werkzeug.middleware.dispatcher import (
    DispatcherMiddleware,
)  
from get_data import get_app
from upload_master_data import master_data
from manully_entry import manully_entry

camcom = get_app()
upload_master_data = master_data()
manully = manully_entry()

application = DispatcherMiddleware(
    camcom,
    {        
        "/upload_master_data": upload_master_data,
        "/manully_entry": manully,
    },
)
