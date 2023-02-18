import pymysql
import pymysql.cursors


class Db():

    def __init__(self):
        DATABASE_HOST="localhost"
        DATABASE_NAME="fast_crud"
        DATABASE_USER="root"
        DATABASE_PASSWORD="pass123"

        self.connection_pool = pymysql.connect(
            host=DATABASE_HOST, 
            user=DATABASE_USER, 
            password=DATABASE_PASSWORD,
            db=DATABASE_NAME
        )
