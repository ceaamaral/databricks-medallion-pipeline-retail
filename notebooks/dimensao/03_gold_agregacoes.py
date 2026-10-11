# Databricks notebook source
# Criando uma visão agregada cruzando Vendas e Lojas
df_gold_store_performance = spark.sql("""
   SELECT s.store_id,
          st.store_name,
          st.city,
          COUNT(s.sale_id) AS total_orders,
          SUM(s.amount) AS total_revenue
     FROM medallion_pipe_retail.silver.sales s
    INNER JOIN medallion_pipe_retail.silver.stores st ON s.store_id = st.store_id
    GROUP BY s.store_id, st.store_name, st.city
""")

df_gold_store_performance.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion_pipe_retail.gold.stores")

display(spark.sql("SELECT * FROM medallion_pipe_retail.gold.stores LIMIT 10"))