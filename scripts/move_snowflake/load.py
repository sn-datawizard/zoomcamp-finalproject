import pandas as pd

import config
import config2
import config_snow
import helpers

# Set variables for MongoDB
password = config.PASS
database = config.DATABASE
collection = config.COLLECTION

# Establish connection to MongoDB database
client = helpers.connect_mongo(password, database)

# Import data from MongoDB database to dataframe
df_population = helpers.read_mongo(client, database, collection)

# Set variables for MongoDB
password2 = config2.PASS
database2 = config2.DATABASE
collection2 = config2.COLLECTION

# Establish connection to MongoDB database
client = helpers.connect_mongo(password2, database2)

# Import data from MongoDB database to dataframe
df_continents = helpers.read_mongo(client, database2, collection2)

# Set parameter for Snowflake upload
account = config_snow.account
username = config_snow.username
password = config_snow.password
warehouse = config_snow.warehouse
database = config_snow.database
schema = config_snow.schema
table1 = "POPULATION_DATA"
table2 = "COUNTRY_DATA"

# Establish Snowflake connection
connection = helpers.connect_snowflake(username, password, account, warehouse, database, schema)
print(connection)

# Upload dataframes
helpers.write_snowflake(connection, df_population, table1)
helpers.write_snowflake(connection, df_continents, table2)
