import pymongo
import pandas as pd
import sqlalchemy
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import time

def connect_mongo(password, database):
    """Establish connection to MongoDB database"""
    client = pymongo.MongoClient(f"mongodb+srv://superuser1:{password}@zoomcamp-finalproject.uae3va7.mongodb.net/{database}?retryWrites=true&w=majority")
    return client


def upload_mongo(client, database, collection, dataframe):
    """Delete current documents in database and upload dataframe to MongoDB database"""
    connection = client
    db = client[f"{database}"]
    collection = db[f"{collection}"]

    dictionary = pd.DataFrame.to_dict(dataframe, orient="records")
    datadelete = collection.delete_many({})
    print(collection.count_documents({}))
    dataload = collection.insert_many(dictionary)
    print(collection.count_documents({}))

def read_mongo(client, database, collection):
    """Export data stored on MongoDB"""
    connection = client
    db = client[f"{database}"]
    collection = db[f"{collection}"]

    data = list(collection.find())
    df = pd.DataFrame(data).drop("_id", axis=1)
    return df   

def connect_snowflake(username, password, account, warehouse, database, schema):
    """Establish connection to Snowflake database"""
    conn = snowflake.connector.connect(
        user=f'{username}',
        password=f'{password}',
        account=f'{account}',
        warehouse=f'{warehouse}',
        database=f'{database}',
        schema=f'{schema}'
    )
    return conn


def write_snowflake(connection, dataframe, table):
    """Import data into Snowflake database"""
    conn = connection
    
    start_time = time.time()
    write_pandas(conn=connection, df=dataframe, table_name=table, auto_create_table=True, overwrite=True)
    print(table)
    print("--- %s seconds ---" % (time.time() - start_time))





