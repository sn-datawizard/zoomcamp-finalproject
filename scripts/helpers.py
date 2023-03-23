import pymongo
import pandas as pd

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
