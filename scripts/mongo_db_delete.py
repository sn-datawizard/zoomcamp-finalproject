import pymongo
import pandas as pd
import config
import config2

def connect_mongo(password, database):
    """Establish connection to MongoDB database"""
    client = pymongo.MongoClient(f"mongodb+srv://superuser1:{password}@zoomcamp-finalproject.uae3va7.mongodb.net/{database}?retryWrites=true&w=majority")
    return client


def delete_mongo(client, database, collection):
    """Delete current documents in database and upload dataframe to MongoDB database"""
    connection = client
    db = client[f"{database}"]
    collection = db[f"{collection}"]

    print(collection.count_documents({}))
    datadelete = collection.delete_many({})
    print(collection.count_documents({}))

password = config2.PASS
database = config2.DATABASE
collection = config2.COLLECTION

# Establish connection to MongoDB database
client = connect_mongo(password, database)

# Upload data to MongoDB database
delete_mongo(client, database, collection)