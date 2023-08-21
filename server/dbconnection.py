# dbconnection.py

import oracledb

def create_connection():
    connection = oracledb.connect(user="kosa13", password="kosa2023oraclE", dsn="edudb_high",
                                  config_dir="C:\Dev\Python\Wallet_edudb",
                                  wallet_location="C:\Dev\Python\Wallet_edudb",
                                  wallet_password="pythonoracle21")
    return connection

connection = create_connection()
cursor = connection.cursor()

def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description]
    def createRow(*args):
        return dict(zip(columnNames, args))
    return createRow
