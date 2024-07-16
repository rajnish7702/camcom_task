import json
import pymysql
from flask import jsonify 
import mysql.connector
from mysql.connector import Error
import pandas as pd



def update_reports(data):
    # connecting with database
    connection = mysql.connector.connect(
        host="localhost",
        user="camcom",
        password="Camcom@123",
        db="reports"
    )
    cursor = connection.cursor()

    
    table_name = 'master_file'
    comman_cn = data['comman_cn']
    batch_no = data['batch_no']
    try:
        sql=f"SELECT * FROM {table_name} WHERE `COMMON_CN_NO.` = {comman_cn} AND `BATCH_NO.` = {batch_no};"

        cursor.execute(sql)
        result = cursor.fetchall()       
        return result[0]
    except:
        return "getting database error "
    finally:
    # Close the connection
        cursor.close()
        connection.close()





def tables_header():
    connection = mysql.connector.connect(
        host="localhost",
        user="camcom",
        password="Camcom@123",
        db="reports"
    )

    cursor = connection.cursor()
    # try:

    cursor.execute('SELECT * FROM master_file LIMIT 1;')
    column_names = [i[0] for i in cursor.description]
    return column_names
    # except:
    #     return "some database error"
    # finally:
    #     cursor.close()
    #     connection.close()


# def adding_cn_qty():

#     column_definitions = ", ".join(
#             [f"`{col}` VARCHAR(255)" if df[col].dtype == object else f"`{col}` INT" for col in df.columns]
#         )

#         # column_definitions_with_pk = f"`id` INT AUTO_INCREMENT PRIMARY KEY, {column_definitions}"
#         # create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({column_definitions_with_pk});"

#         # cursor.execute(create_table_sql)



def add_utils(data):
    cn_qty = data['cn_qty']
