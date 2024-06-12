import json
import pymysql
from flask import jsonify 
import mysql.connector
from mysql.connector import Error
import pandas as pd


 

def connect_db():
    """ connection mysql db """

    try:   
        connection = mysql.connector.connect(
            host="localhost",
            user="zydus",
            password="zydus@123",
            db="world"
        )
        return connection.cursor()

    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


def fetch_data():
    connection = connect_db()
    
    if connection is None:
        return jsonify({"error": "Failed to connect to database"}), 500

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM city")
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()

   

    return jsonify(rows)




def create_table_insert_recode(data_frame):

    # connecting with database
    connection = mysql.connector.connect(
        host="localhost",
        user="zydus",
        password="zydus@123",
        db="Zydus_Products"
    )

    # cursor object
    cursor = connection.cursor()

    df = pd.read_excel(data_frame)  
    # table name
    table_name = 'camcom_products'

    df = df.dropna(axis=1, how='any')
    
    df = df.where(pd.notnull(df), None)

    try:
        # table creating
        
        # column_definitions = ", ".join(
        #     [f"`{col}` VARCHAR(255)" if df[col].dtype == object else f"`{col}` INT" for col in df.columns]
        # )
        # create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({column_definitions});"

        # cursor.execute(create_table_sql)
        

        # data is inserting
        insert_sql = f"INSERT INTO `{table_name}` ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(df.columns))})"
        for row in df.itertuples(index=False, name=None):
            cursor.execute(insert_sql, row)
        return "records inserted"

    except:
        return "sql syntex is worng"
    
    finally:

        connection.commit()

        # Close the connection
        cursor.close()
        connection.close()
    




