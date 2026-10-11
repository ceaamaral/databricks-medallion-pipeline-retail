# 🚀 Pipeline de Engenharia de Dados com Databricks e Arquitetura Medallion

Este repositório apresenta um projeto prático de Engenharia de Dados desenvolvido para demonstrar a implementação de um pipeline corporativo ponta a ponta (*end-to-end*). O projeto utiliza **Databricks**, **PySpark** e **Delta Lake**, aplicando os conceitos fundamentais da **Arquitetura Medallion (Bronze, Silver e Gold)**.

---

## 📋 1. O Problema de Negócio
Uma empresa do setor varejista enfrenta desafios na consolidação de seus dados operacionais de vendas e logística, que chegam de fontes heterogêneas (arquivos CSV e JSON legados). O objetivo deste projeto é automatizar a ingestão, garantir a qualidade, limpar inconsistências e estruturar os dados em camadas analíticas confiáveis, permitindo que equipes de negócio e analistas consumam métricas consolidadas de forma rápida e segura.

---

## 🏗️ 2. Arquitetura da Solução (Medallion Architecture)

O fluxo de dados foi estruturado em três camadas distintas no **Delta Lake**:

1. **Camada Bronze (Raw):** 
   - Recebe os dados brutos oriundos das fontes (CSV/JSON) sem alterações estruturais.
   - Adiciona metadados essenciais de rastreabilidade e auditoria (como `ingestion_timestamp` e `source_file`).
2. **Camada Silver (Enriched / Cleansed):** 
   - Realiza a limpeza de dados (remoção de duplicadas, tratamento de valores nulos e inválidos).
   - Padroniza formatos de data, tipagens e maiúsculas/minúsculas.
   - Aplica particionamento estratégico para otimização de consultas.
3. **Camada Gold (Aggregated / Business-Ready):** 
   - Contém tabelas agregadas e modelos dimensionais prontos para consumo por ferramentas de BI (como Power BI) e equipes de Analytics.

---

## 🛠️ 3. Tecnologias Utilizadas
* **Linguagem:** Python & SQL
* **Processamento Distribuído:** Apache Spark / PySpark
* **Plataforma de Dados:** Databricks (Community / Cloud)
* **Storage & Formato de Tabelas:** Delta Lake
* **Controle de Versão:** Git & GitHub

---

## ⚙️ 4. Estrutura do Pipeline

```text
[ Fontes Brutas: CSV / JSON ] 
           │
           ▼
   (Camada BRONZE) ──> Ingestão crua + Metadados de Auditoria
           │
           ▼
   (Camada SILVER) ──> Limpeza, Tipagem, Tratamento de Nulos & Particionamento
           │
           ▼
    (Camada GOLD)  ──> Agregações de Negócio para Indicadores e BI
