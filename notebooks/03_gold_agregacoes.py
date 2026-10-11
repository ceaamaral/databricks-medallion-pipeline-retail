# Criando uma tabela agregada de Vendas por Estado e Status para consumo analítico
df_gold_sales_by_state = spark.sql("""
    SELECT 
        customer_state,
        status,
        COUNT(sale_id) AS total_orders,
        SUM(amount) AS total_revenue,
        AVG(amount) AS avg_ticket
    FROM medallion_pipe_retail.silver.sales
    GROUP BY customer_state, status
""")

# Gravando na Camada Gold
df_gold_sales_by_state.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("medallion_pipe_retail.gold.sales")

display(spark.sql("SELECT * FROM medallion_pipe_retail.gold.sales"))
