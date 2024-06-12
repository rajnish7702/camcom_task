import requests
import json
import mysql.connector
from mysql.connector import Error
from upload_master_data.utils import connect_db


def get_cn(id):
    # cursor  = connect_db()

    connection = mysql.connector.connect(
        host="localhost",
        user="zydus",
        password="zydus@123",
        db="Zydus_Products"
    )
    # creating cursor object to performe operation on sql 

    cursor = connection.cursor()
    try:
        # sql query 

        sql=f"SELECT * FROM camcom_products where COMMON_CN_NO={id}"
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows
    except:

        # if any issue occured with fetching with database we are providing with some message to know end user
        return "fetching data sql syntext is wrong"
    finally:
        # colsing database connection
        cursor.close()
        cursor.close()



def party_infomation(data):
    # connectinf with database 

    connection = mysql.connector.connect(
        host="localhost",
        user="zydus",
        password="zydus@123",
        db="Zydus_Products"
    )
    # creating cursor object to performe operation on sql 
    cursor = connection.cursor()
    plt = data['plt']
    comman_cn = data['comman_cn']
    batch_no = data['batch_no']
   
    try:
        # sql query 
        sql=f"SELECT * FROM camcom_products where PLNT={plt} AND COMMON_CN_NO={comman_cn} AND BATCH_NO={batch_no};"
        cursor.execute(sql)
        rows = cursor.fetchone()

        return rows
    except:
        # if any issue occured with fetching with database we are providing with some message to know end user
        return "Fetching data is not not batch"
    finally:
        # colsing database connection
        cursor.close()
        cursor.close()
        

