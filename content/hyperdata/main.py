import hyperdata.visualize as visualize
import hyperdata.db as dbconnector

def plot(stream_name,table_name):
    df = dbconnector.read_table(table_name,dbconnector.load_credentials())
    visualize.animate(stream_name,df)

def data(stream_name,table_name):
    df = dbconnector.read_table(table_name,db.load_credentials())
    return df