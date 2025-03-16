# **Netflix Data Engineering Project**  

## **Overview**  
This project demonstrates an **end-to-end Data Engineering pipeline** for Netflix data using **Azure Data Factory, Databricks, PySpark, Apache Spark, Delta Live Tables, and Azure Synapse Analytics**. The pipeline efficiently ingests, processes, and stores Netflix data incrementally for reporting and analytics.  

## **Technologies Used**  
- **Azure Data Factory** – Orchestration of data ingestion.  
- **Databricks (Apache Spark, PySpark)** – Scalable data transformation.  
- **Azure Data Lake Gen2** – Efficient cloud-based data storage.  
- **Delta Live Tables (DLT)** – Real-time data transformation and management.  
- **Apache Spark SQL** – Querying and data analysis.  
- **Azure Synapse Analytics** – Data warehousing and analytical processing.  
- **Power BI** – Data visualization and reporting.  
- **GitHub** – Version control for source code.  
- **Security & Access Control** – Implemented using **Azure Active Directory** and **Key Vault**.  

## **Architecture & Workflow**  
The project follows a **multi-layered architecture** to process data in structured layers:  

### **1. Data Ingestion**  
- **Data Sources**: Netflix data is ingested from various sources using **Azure Data Factory**.  
- **Storage**: Raw data is stored in **Azure Data Lake Gen2**.  
- **Automation**: **Databricks AutoLoader** enables efficient incremental data ingestion.  

### **2. Data Transformation**  
- **Raw Data (Bronze Layer)**: Stored in **Parquet format** in the data lake.  
- **Transformed Data (Silver Layer)**:  
  - Data is processed using **Databricks (PySpark, Apache Spark)**.  
  - Business logic, filtering, and transformations are applied.  
  - Workflows and activities like **ForEach & If-Else** are implemented.  
- **Processed Data (Gold Layer)**:  
  - Data is stored in **Delta Lake** using **Delta Live Tables (DLT)**.  
  - **Star Schema** is implemented for optimized querying.  

### **3. Data Warehousing & Reporting**  
- **Azure Synapse Analytics**:  
  - Processed data is moved to **Synapse Warehouse** for analytical queries.  
  - Optimized for large-scale data processing.  
- **Power BI**:  
  - Used for creating dashboards and visualizing Netflix analytics.  

## **Key Features**  
✅ **Incremental Data Processing** using AutoLoader  
✅ **Delta Lake Architecture** with Bronze, Silver, and Gold layers  
✅ **Dynamic & Parameterized Pipelines** for processing multiple datasets  
✅ **Data Quality Rules** using `dlt.expect_all_or_drop()`  
✅ **Global & Temporary Views** for easy querying  
✅ **Streaming & Batch Processing** support  
✅ **Power BI Reporting Dashboard**  

## **Data Flow**  
1. **Raw Data Ingestion**: Netflix dataset ingested using Azure Data Factory and Databricks AutoLoader.  
2. **Bronze Layer**: Data stored in Azure Data Lake Gen2 as raw CSV files.  
3. **Silver Layer**:  
   - Data transformation using **PySpark** (data type casting, missing values handling, lookup tables, etc.).  
4. **Gold Layer**:  
   - Star schema modeling, ranking, flagging, and **Delta Live Tables (DLT)** streaming ingestion.  
5. **Azure Synapse**: Aggregated data stored for analysis.  
6. **Power BI Reporting**: Final insights visualized in Power BI.  

## **Code Snippets**  

### **AutoLoader - Incremental Data Load**  
```python
checkpoint_location = "abfss://silver@netflixprojectdlsg.dfs.core.windows.net/checkpoint"
df = spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation", checkpoint_location)\
  .load("abfss://raw@netflixprojectdlsg.dfs.core.windows.net")
display(df)
```

### **Silver Layer Transformation**  
```python
df = df.withColumn("Shorttitle", split(col('title'), ':')[0])
df = df.withColumn("type_flag", when(col('type') == 'Movie', 1)
                              .when(col('type') == 'TV Show', 2)
                              .otherwise(0))
```

### **Gold Layer - Delta Live Tables**  
```python
@dlt.table(name = "gold_netflixdirectors")
@dlt.expect_all_or_drop({"rule1": "show_id is NOT NULL"})
def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdlsg.dfs.core.windows.net/netflix_directors")
    return df
```

## **Setup Instructions**  
1. **Clone the repository**:  
   ```sh
   git clone https://github.com/HareenaChowdary/Netflix-Data-Engineering.git
   ```
2. **Set up Azure services** (Data Factory, Databricks, Data Lake, Synapse, Power BI).  
3. **Configure Databricks Workflows** and **Delta Live Tables (DLT)**.  
4. **Run Azure Data Factory pipeline** to ingest data.  
5. **Execute Databricks notebooks** for transformation.  
6. **Load processed data into Azure Synapse**.  
7. **Visualize data in Power BI**.  

## **Future Enhancements**  
🚀 Implement **Real-time Processing** using **Azure Event Hub**  
🚀 Enhance **Data Quality Checks** with **Great Expectations**  
🚀 Optimize **Synapse Query Performance** with **Materialized Views**  


---
