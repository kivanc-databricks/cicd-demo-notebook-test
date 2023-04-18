# Databricks notebook source
# MAGIC %run ../my_notebooks/Code1

# COMMAND ----------

# MAGIC %run ../my_notebooks/Code2

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text("num", "5")

# COMMAND ----------

param = int(dbutils.widgets.get("num"))

# COMMAND ----------

param

# COMMAND ----------

generate_data1(n=param)
display(spark.sql("select * from my_cool_data"))
