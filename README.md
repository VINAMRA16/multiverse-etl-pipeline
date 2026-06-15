# 🌌 Multiverse ETL Archive (Rick and Morty API)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow.svg)

## 📌 Executive Summary
An end-to-end Python ETL (Extract, Transform, Load) pipeline that harvests, sanitizes, and vaults character data from the Rick and Morty REST API. The engine features automatic pagination, nested JSON flattening, defensive string sanitization, and automated multi-tab Excel report generation.

## 🏗️ Architecture Blueprint
1. **Extraction (`extract.py`):** Utilizes dynamic `while`-loop pagination to harvest records across multiple API pages, implementing stealth rate-limiting (`time.sleep`) to ensure server compliance.
2. **Transformation (`transform.py`):** Leverages `pandas` to un-nest deeply layered JSON dictionaries (e.g., origin planets) and applies vectorized defensive sanitization to all text fields.
3. **Loading (`load.py`):** Executes an idempotent SQLite database ingestion. Utilizes UPSERT logic (`ON CONFLICT DO UPDATE`) anchored by unique API character IDs to guarantee zero data duplication on pipeline reruns.
4. **Analytics (`analytics.py`):** Queries the relational vault and executes Pandas aggregations to automatically generate a multi-tab Executive Excel Report (`.xlsx`) tracking Species Demographics and Life Status.

## 🚀 Execution
```bash
# Run the core ETL pipeline to vault the data
python main.py

# Run the analytics engine to generate the Excel report
python analytics.py