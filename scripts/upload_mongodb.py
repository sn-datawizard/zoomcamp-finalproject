import pandas as pd
import pymongo
import json
import config
import helpers
import requests


# Set up initial parameters for the API call
url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL'
params = {'format': 'json', 'per_page': 100}

# Make the initial API call to get the first page of data
response = requests.get(url, params=params)
data = response.json()
print(f'Page 1 of {data[0]["pages"]} retrieved')

# Iterate through all pages of data and extract the relevant information
page = 2
while page <= data[0]['pages']:
    params['page'] = page
    response = requests.get(url, params=params)
    data += response.json()
    print(f'Page {page} of {data[0]["pages"]} retrieved')
    page += 1


# Iterate over dataframe and add single records to list
data_list = []
for page_idx in range(1, len(data), 2):
    page_data = data[page_idx]
    for entry in page_data:
        year = entry['date']
        country = entry['country']['value']
        population = entry['value']
        data_list.append({'year': year, 'country': country, 'population': population})

# Create dataframe from list
df = pd.DataFrame(data_list)

# Set variables for MongoDB upload
password = config.PASS
database = config.DATABASE
collection = config.COLLECTION

# Establish connection to MongoDB database
client = helpers.connect_mongo(password, database)

# Upload data to MongoDB database
helpers.upload_mongo(client, database, collection, df)


