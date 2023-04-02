import pandas as pd
import findspark
from pyspark.sql import SparkSession
import os

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

# Join dataframes for transfromations
df_population.rename(columns={'year': 'Year', 'country': 'Country', 'population': 'Population'}, inplace=True)
df = pd.merge(left=df_population, right=df_continents, how='left', on='Country')

# Fill NaN values with custom value
df['Continent'].fillna('NONE', inplace=True)
df['Region'].fillna('NONE', inplace=True)
df['Population'].fillna(0.0, inplace=True)

# Create pyspark session
#findspark.init('C:\spark-3.3.0-bin-hadoop3')
#os.environ['SPARK_HOME'] = 'C:\spark-3.3.0-bin-hadoop3'
#os.environ["JAVA_HOME"] = 'C:\Program Files\Java\jdk-18.0.1.1'

spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

# Create pyspark dataframes and SQL table
spark_df = spark.createDataFrame(df)
spark_df.registerTempTable('table1')

# Perform growth rate % calculation
df_final = spark.sql("""
WITH yearly_pop AS (
    SELECT Year, Country, Continent, Region, CAST(Population AS int),
           LAG(CAST(Population AS int)) OVER (PARTITION BY Country ORDER BY Year) AS prev_population
    FROM table1
    WHERE Continent != 'NONE' AND Year = (SELECT MIN(Year) FROM table1) OR Continent != 'NONE' AND Year = (SELECT MAX(Year) FROM table1)
), 
yoy_growth AS (
    SELECT Year, Country, Continent, Region, Population,
           ((Population - prev_population) / prev_population) * 100 AS yoy_growth_pct,
           Population - prev_population AS yoy_growth_abs
    FROM yearly_pop
    WHERE prev_population IS NOT NULL
)
SELECT Year, Country, Continent, Region, Population, yoy_growth_pct, yoy_growth_abs
FROM yoy_growth
ORDER BY Country, Year
""")

# Convert spark dataframe to pandas dataframe
df_transformed = df_final.toPandas()

# Set parameter for Snowflake upload
account = config_snow.account
username = config_snow.username
password = config_snow.password
warehouse = config_snow.warehouse
database = config_snow.database
schema = config_snow.schema

table3 = "GROWTH_DATA"

# Establish Snowflake connection
connection = helpers.connect_snowflake(username, password, account, warehouse, database, schema)

# Upload dataframes
helpers.write_snowflake(connection, df_transformed, table3)


