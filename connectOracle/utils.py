import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

def check_connection() -> str:
    oracledb.init_oracle_client()
    connection = oracledb.connect(  user=os.getenv("DB_USER"), 
                                    password=os.getenv("DB_PASSWORD"), 
                                    dsn=os.getenv("DB_DSN") )
    cursor  = connection.cursor()

    version = "Database version: " + connection.version
    cursor.close()
    return version

def sql_query(query : str) -> tuple:
    oracledb.init_oracle_client()
    connection = oracledb.connect(  user=os.getenv("DB_USER"), 
                                password=os.getenv("DB_PASSWORD"), 
                                dsn=os.getenv("DB_DSN") )
    cursor  = connection.cursor()

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close
    return result