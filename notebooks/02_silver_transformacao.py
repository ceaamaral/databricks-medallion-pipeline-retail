from pyspark.sql.functions import col, to_date, upper, when

# Lendo da camada Bronze
df_bronze = spark.read.table("medallion_pipe_retail.bronze.sales")

# Limpeza e Transformação
df_silver = df_bronze \
    .dropDuplicates() \
    .filter(col("sale_id").isNotNull() & (col("amount") > 0)) \
    .withColumn("sale_date", to_date(col("date_string"), "yyyy-MM-dd")) \
    .withColumn("customer_state", upper(col("customer_state"))) \
    .withColumn("status", 
                when(col("shipping_status") == "Delivered", "Entregue")
                .otherwise("Pendente")) \
    .select("sale_id", "customer_id", "store_id", "sale_date", "amount", "customer_state", "status")

# Gravando na Camada Silver com otimização Delta
df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .partitionBy("customer_state") \
    .saveAsTable("medallion_pipe_retail.silver.sales")

display(spark.sql("SELECT * FROM medallion_pipe_retail.silver.sales LIMIT 10"))
