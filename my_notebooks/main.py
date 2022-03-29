# Databricks notebook source
# MAGIC %run ../my_notebooks/Code1

# COMMAND ----------

# MAGIC %run ../my_notebooks/Code2

# COMMAND ----------

generate_data1()
display(spark.sql("select * from my_cool_data"))
