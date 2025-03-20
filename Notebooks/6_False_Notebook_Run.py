# Databricks notebook source
var = dbutils.jobs.taskValues.get(
    taskKey="Weekday_Lookup",
    key="week_output",
    debugValue="default_value"
)

# COMMAND ----------

print(var)