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
            user="camcom",
            password="Camcom@123",
            db="reports"
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




def create_table_insert_recode(master_file,location):
    # connecting with database
    connection = mysql.connector.connect(
        host="localhost",
        user="camcom",
        password="Camcom@123",
        db="zydus"
    )
    cursor = connection.cursor()

    df = pd.read_excel(master_file)

    df.columns = df.columns.str.replace(' ', '_')
    df.insert(17, "Location", location, True)

    table_name = 'reports'
    try:

        # column_definitions = ", ".join(
        #     [f"`{col}` VARCHAR(255)" if df[col].dtype == object else f"`{col}` INT" for col in df.columns]
        # )
        # print(column_definitions)
        # column_definitions_with_pk = f"`id` INT AUTO_INCREMENT PRIMARY KEY, {column_definitions}"
        # create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({column_definitions_with_pk});"

        # cursor.execute(create_table_sql)

        # Inserting data
        insert_sql = f"INSERT INTO `{table_name}` ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(df.columns))})"
        for row in df.itertuples(index=False, name=None):
            cursor.execute(insert_sql, row)

        connection.commit()
        return "Records inserted successfully"
    except:
        return "getting error "
    finally:
    # Close the connection
        cursor.close()
        connection.close()
