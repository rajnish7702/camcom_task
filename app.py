from werkzeug.middleware.dispatcher import (
    DispatcherMiddleware,
)  
from get_data import get_app
from upload_master_data import master_data
camcom = get_app()
upload_master_data = master_data()


application = DispatcherMiddleware(
    camcom,
    {        
        "/upload_master_data": upload_master_data,

    },
)
