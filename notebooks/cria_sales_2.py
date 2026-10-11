import random
import csv

# Configurando semente para reprodutibilidade
random.seed(42)

states = ["RJ", "SP", "MG", "ES", "BA", None] # Incluindo valor nulo
statuses = ["Delivered", "Pending", "Cancelled", "Unknown"]

rows = []
base_sale_id = 200

for i in range(1, 101):
    sale_id = base_sale_id + i
    # Injetando alguns valores nulos no ID ou no Estado de vez em quando
    if i % 15 == 0:
        sale_id = None
        
    customer_id = random.randint(500, 550)
    store_id = random.randint(1, 3)
    
    # Injetando datas inválidas ou nulas
    if i % 20 == 0:
        date_string = "2026-02-31" # Data inválida (fevereiro não tem 31)
    elif i % 25 == 0:
        date_string = None
    else:
        date_string = f"2026-10-{random.randint(1, 10):02d}"
        
    # Injetando valores negativos ou zero (inválidos para vendas)
    if i % 10 == 0:
        amount = round(random.uniform(-150.0, 0.0), 2)
    elif i % 30 == 0:
        amount = None
    else:
        amount = round(random.uniform(50.05, 1500.0), 2)
        
    shipping_status = random.choice(statuses)
    customer_state = random.choice(states)
    
    row = [sale_id, customer_id, store_id, date_string, amount, shipping_status, customer_state]
    rows.append(row)

# Injetando propositalmente algumas linhas totalmente duplicadas
for _ in range(5):
    rows.append(random.choice(rows))

# Gravando o arquivo sales_2.csv
header = ["sale_id", "customer_id", "store_id", "date_string", "amount", "shipping_status", "customer_state"]

with open("sales_2.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Arquivo sales_2.csv gerado com sucesso contendo mais de 100 linhas (com sujeiras injetadas)!")
