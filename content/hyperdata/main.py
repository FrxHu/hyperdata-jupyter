import visualize
import db

def plot(stream_name,table_name):
    df = db.read_table(table_name,db.load_credentials())
    visualize.animate(stream_name,df)

def data(stream_name,table_name):
    df = db.read_table(table_name,db.load_credentials())
    return df