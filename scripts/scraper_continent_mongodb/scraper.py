import requests
from bs4 import BeautifulSoup
import pandas as pd
import config2
import helpers

# Set the user agent string to use in the request header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a GET request to the webpage URL with the user agent header
url = 'https://statisticstimes.com/geography/countries-by-continents.php'
response = requests.get(url, headers=headers)
print(response.status_code)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the country and continent data
table = soup.find('table', id='table_id')

# Extract the rows of the table
rows = table.find_all('tr')
row = rows[1]
print(row)

num_rows = len(rows)
country_list = []
continent_list = []
region_list = []

for row in rows[1:]:
    names = row.find_all('td', {'class': 'name'})
    country = names[0].text
    continent = names[3].text
    region = names[1].text
    #print(str(country) + ' | ' + str(continent) + ' | ' + str(region))

    country_list.append(country)
    continent_list.append(continent)
    region_list.append(region)


# Create an empty Pandas DataFrame to store the data
df = pd.DataFrame(data=country_list, columns=['Country'])
df['Continent'] = continent_list
df['Region'] = region_list

# Print the DataFrame to the console
print(df)

# Set auth and config variables
password = config2.PASS
database = config2.DATABASE
collection = config2.COLLECTION

# Establish mongoDB connection
client = helpers.connect_mongo(password, database)

# Upload dataframe to MongoDB
helpers.upload_mongo(client, database, collection, df)