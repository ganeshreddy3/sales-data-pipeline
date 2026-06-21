# 🚀 How to Run the Project

## Prerequisites

Make sure the following are installed:

* Python 3.12+
* PostgreSQL
* Apache Airflow
* Git

---

# 1. Clone the Repository

```bash
git clone <your-repository-url>
cd sales-data-pipeline
```

---

# 2. Activate Project Environment

```bash
source venv/bin/activate
```

Install dependencies if required:

```bash
pip install -r requirements.txt
```

---

# 3. Start PostgreSQL

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

# 4. Run the Sales ETL Pipeline

```bash
python main.py
```

This pipeline:

```text
sales.csv
   ↓
Extract
   ↓
Transform
   ↓
Load PostgreSQL
```

---

# 5. Run Fake Store API Pipeline

```bash
python test_products_load.py
```

This pipeline:

```text
Fake Store API
      ↓
Extract
      ↓
Transform
      ↓
Load PostgreSQL
```

---

# 6. Launch Streamlit Dashboard

Open a new terminal:

```bash
cd sales-data-pipeline

source venv/bin/activate

streamlit run dashboard/app.py
```

Open in browser:

```text
http://localhost:8501
```

---

# 7. Start Apache Airflow

## Terminal 1 - Webserver

```bash
source ~/Documents/Projects/airflow_venv/bin/activate

export AIRFLOW_HOME=~/airflow

airflow webserver --port 8080
```

---

## Terminal 2 - Scheduler

```bash
source ~/Documents/Projects/airflow_venv/bin/activate

export AIRFLOW_HOME=~/airflow

airflow scheduler
```

---

# 8. Open Airflow UI

Open:

```text
http://localhost:8080
```

Login using your Airflow credentials.

---

# 9. Trigger ETL Workflow

1. Search for:

```text
sales_etl_pipeline
```

2. Enable the DAG.
3. Click **Trigger DAG**.

Airflow will automatically execute the ETL pipeline.

---

# Verify Data in PostgreSQL

Connect:

```bash
sudo -u postgres psql -d sales_db
```

Check sales data:

```sql
SELECT COUNT(*) FROM sales;
```

Check product data:

```sql
SELECT COUNT(*) FROM products;
```

---

# View Pipeline Logs

```bash
cat logs/pipeline.log
```

Example:

```text
INFO - Pipeline Started
INFO - Pipeline Completed
```

---

# Project Architecture

```text
                 +----------------+
                 | sales.csv      |
                 +----------------+
                          |
                          v
                 +----------------+
                 | ETL Pipeline   |
                 +----------------+
                          |
                          v
                 +----------------+
                 | PostgreSQL     |
                 +----------------+
                          ^
                          |
                 +----------------+
                 | Fake Store API |
                 +----------------+

                          |
                          v

                 +----------------+
                 | Apache Airflow |
                 +----------------+

                          |
                          v

                 +----------------+
                 | Streamlit      |
                 | Dashboard      |
                 +----------------+
```

---

# Useful URLs

### Streamlit Dashboard

```text
http://localhost:8501
```

### Apache Airflow

```text
http://localhost:8080
```
