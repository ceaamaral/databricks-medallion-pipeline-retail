# Databricks notebook source
# Leitura do JSON bruto de Lojas
raw_stores_path = "/Volumes/workspace/default/raw_data/stores.json"

df_stores_raw = spark.read \
    .option("multiline", "true") \
    .json(raw_stores_path)

# Gravando na Camada Bronze (Delta Lake)
df_stores_raw.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion_pipe_retail.bronze.stores")

display(spark.sql("SELECT * FROM medallion_pipe_retail.bronze.stores LIMIT 10"))