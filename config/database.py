from databases import Database
# from app.env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
import aiomysql

from sqlalchemy import select
from .db import db_config


db_conn_string = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8&connection_timeout=10' % (
    db_config.user,
    db_config.password,
    db_config.host,
    db_config.database,
)
# print("\n")
# print(db_conn_string)               
# print("\n")

database =  Database(db_conn_string, min_size=5, max_size=20)
