# How to Run the Project

## 1. Start PostgreSQL

```bash
sudo systemctl start postgresql
```

Verify:

```bash
sudo systemctl status postgresql
```

Expected:

```text
active (running)
```

---

## 2. Run the ETL Pipeline

Open a terminal:

```bash
cd ~/Documents/Projects/sales-data-pipeline

source venv/bin/activate

python main.py
```

This will:

* Extract data from CSV
* Transform and clean data
* Save processed data
* Load data into PostgreSQL

---

## 3. Launch the Streamlit Dashboard

Open a new terminal:

```bash
cd ~/Documents/Projects/sales-data-pipeline

source venv/bin/activate

streamlit run dashboard/app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## 4. Start Apache Airflow

### Terminal 1 - Webserver

```bash
source ~/Documents/Projects/airflow_venv/bin/activate

export AIRFLOW_HOME=~/airflow

airflow webserver --port 8080
```

### Terminal 2 - Scheduler

```bash
source ~/Documents/Projects/airflow_venv/bin/activate

export AIRFLOW_HOME=~/airflow

airflow scheduler
```

Open in browser:

```text
http://localhost:8080
```

Login using your Airflow credentials.

---

## 5. Trigger ETL Pipeline from Airflow

1. Open Airflow UI
2. Search for:

```text
sales_etl_pipeline
```

3. Enable the DAG
4. Click **Trigger DAG**

Airflow will automatically execute the ETL workflow.

---

## Useful URLs

### Streamlit Dashboard

```text
http://localhost:8501
```

### Apache Airflow

```text
http://localhost:8080
```

---

## Check Logs

```bash
cat logs/pipeline.log
```

Example:

```text
INFO - Pipeline Started
INFO - Pipeline Completed
```

---

## Verify Data in PostgreSQL

```bash
sudo -u postgres psql -d sales_db
```

Run:

```sql
SELECT COUNT(*) FROM sales;
```
# Sales Data Pipeline

An end-to-end Data Engineering project that:

- Extracts sales data from CSV files
- Cleans and transforms the data
- Loads it into PostgreSQL
- Generates reports
- Displays dashboards
- Automates workflows using Apache Airflow

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Streamlit
