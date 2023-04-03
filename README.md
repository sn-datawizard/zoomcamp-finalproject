# End-to-end data pipeline

## Problem statement
The world's population has been growing at an unprecedented rate. Understanding this growth and its impact on different continents and countries is crucial. Therefore, the problem is to create an informative and comprehensive visualization of world population and population growth for different continents and countries from 1960 to 2021. 

The visualization should provide insights into how population growth has evolved over time, which continents and countries have experienced the most significant growth, and how growth rates have varied across regions. 

Furthermore, the visualization should be intuitive and accessible to a wide range of audiences to help inform decision-making and raise awareness about population issues.

### Data sources:
World Bank Data API (https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
Webpage with world continent data (https://statisticstimes.com/geography/countries-by-continents.php)

## Technologies used
**Cloud**: Google Cloud (GCP)

**Infrastructure as code (IaC)**: Terraform

**Workflow orchestration**: Docker, GCP Kubernetes Engine

**Data Wareshouse**: Snowflake

**Data Lake**: MongoDB Atlas

**Batch processing**: Python, Spark

**Transformations**: Python, Spark

## Data Pipeline Diagram
PNG

## Dashboard
The visualization can be accessed here: **https://lookerstudio.google.com/s/h6FpjThM-Zw**

PNG

## Future development ideas
- The dataset can be extended by Immigrants, Emigrants and unemployment rate data
- With the extended dataset further analyisis/statistics can be performed, for instance, correlation
- Furthermore a prediction for future population can be implemented