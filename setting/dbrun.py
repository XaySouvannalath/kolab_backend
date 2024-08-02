import mysql.connector
from config.db import db_config



def connect():
    return mysql.connector.connect(
        host=db_config.host,
        user=db_config.user,
        password=db_config.password,
        database=db_config.database
    )
    

conn = connect()
cursor = conn.cursor()