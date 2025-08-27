from databases import Database
# from app.env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
import aiomysql

from sqlalchemy import select
from .db import db_config


# Using aiomysql directly with better configuration
db_conn_string = (
    f'mysql://{db_config.user}:{db_config.password}@{db_config.host}/{db_config.database}'
    f'?minsize=2'
    f'&maxsize=10'
    f'&pool_recycle=3600'
    f'&connect_timeout=30'
    f'&autocommit=1'
    f'&charset=utf8mb4'
)

database = Database(db_conn_string)