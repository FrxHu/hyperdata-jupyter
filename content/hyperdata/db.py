import piplite
await piplite.install(["psycopg2", "python-dotenv"])
import os 
import psycopg2 as db
from dotenv import load_dotenv
import pandas as pd

def load_credentials():
    load_dotenv()
    creds = {
        'db_user' : os.getenv('db_user'),
        'db_password' : os.getenv('db_password'),
        'db_host' : os.getenv('db_host'),
        'db_port' : os.getenv('db_port'),
        'db_name' : os.getenv('db_name')
    }
    return creds

def read_table(name,creds):
    conn = db.connect(user=creds['db_user'],password=creds['db_password'],host=creds['db_host'],port=creds['db_port'],database=creds['db_name'])
    df = pd.read_sql(f'select * from {name}',conn)
    return df
