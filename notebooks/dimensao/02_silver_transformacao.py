# Databricks notebook source
from pyspark.sql.functions import col, upper

df_stores_bronze = spark.read.table("bronze_stores")

df_silver_stores = df_stores_bronze \
    .dropDuplicates() \
    .filter(col("store_id").isNotNull()) \
    .withColumn("city", upper(col("city")))

df_silver_stores.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion_pipe_retail.silver.stores")

display(spark.sql("SELECT * FROM medallion_pipe_retail.silver.stores LIMIT 10"))