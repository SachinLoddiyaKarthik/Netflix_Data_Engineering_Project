# Databricks notebook source
# MAGIC %md
# MAGIC # DLT Notebook - Gold Layer

# COMMAND ----------

looktables_rules = {
    "rule1", "show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_directors"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunction():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdlsachin.dfs.core.windows.net/netflix_directors")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_cast"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunction():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdlsachin.dfs.core.windows.net/netflix_cast")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_countries"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunction():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdlsachin.dfs.core.windows.net/netflix_countries")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_category"
)
@dlt.expect_all_or_drop("rule1" : "show_id is NOT NULL")
def myfunction():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdlsachin.dfs.core.windows.net/netflix_category")
    return df

# COMMAND ----------

@dlt.table

def gold_stg_netflix_titles():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdlsachin.dfs.core.windows.net/netflix_titles")
    return df


# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

@dlt.view

def gold_trns_netflix_titles():
    df = spark.readStream.table("LIVE.gold_stg_netflix_titles")
    df = df.withColumn("newflag",lit(1))
    return df


# COMMAND ----------

master_data_rules = {
    "rule1", "newflag is NOT NULL"
    "rule2", "show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table
@dlt.expect_all_or_drop(master_data_rules)
def gold_netflix_titles():
    df = spark.readStream.table("LIVE.gold_trns_netflix_titles")
    return df