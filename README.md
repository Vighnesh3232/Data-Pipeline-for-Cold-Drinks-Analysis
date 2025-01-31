# Data Engineering Project - Cold Drinks Data Pipeline

## 📌 Overview
This repository contains an **ETL pipeline** built using **Apache Airflow** and executed within **WSL (Windows Subsystem for Linux)**. The pipeline is designed to extract, transform, and analyze **Cold Drinks Market Data**, providing insights into consumer behavior and market trends.

## 🚀 Project Workflow
1. **Data Extraction**: Loads raw data from multiple CSV files in a directory.
2. **Data Transformation**: Performs cleaning, data type conversion, and various analyses.
3. **Data Loading**: Stores processed results into structured files.
4. **Automated Execution**: The pipeline runs on **Apache Airflow**, ensuring scheduled execution.

## 📁 Project Structure
📂 Data-Engineering-Project │-- 📄 README.md (This file) │-- 📂 Data │ │-- Processed_Cold_Drinks_Data.csv (Processed data output) │-- 📂 Scripts │ │-- etl_dag.py (Airflow DAG for ETL process) │ │-- etl_script.py (ETL logic implementation) │ │-- wrapper_script.sh (Shell script to trigger ETL execution) │-- 📂 airflow │ │-- input_data/ (Directory for raw data) │ │-- extract_folder/ (Directory for extracted/processed data) │-- 📂 logs (Airflow logs) │-- 📂 dags (Airflow DAGs folder)


## 🛠️ Technologies Used
- **Apache Airflow** - Workflow orchestration
- **Python (pandas, matplotlib)** - Data processing and visualization
- **WSL (Windows Subsystem for Linux)** - Execution environment
- **Bash (Shell Scripting)** - Automating script execution

## 📊 ETL Pipeline Components

### 1️⃣ **Airflow DAG (etl_dag.py)**
Defines an **ETL workflow** using Airflow, scheduling tasks for data extraction, transformation, and analysis.

### 2️⃣ **ETL Script (etl_script.py)**
Contains functions for:
- **Loading data** from multiple CSVs
- **Analyzing Age vs Frequency** of consumption
- **Identifying effective marketing channels** by age group
- **Understanding packaging preferences** for health-conscious consumers
- **Examining taste ratings vs price range**
- **Analyzing urban vs rural barriers** to trying new brands

### 3️⃣ **Wrapper Script (wrapper_script.sh)**
Executes the **ETL pipeline** using a shell script in **WSL**.

## 🔄 How to Run the Project
1. **Set up Apache Airflow**:
   ```bash
   pip install apache-airflow
   airflow db init
   airflow webserver -p 8080 &
   airflow scheduler &


Sure! Here is your complete README.md file in markdown code format:

markdown
Copy
Edit
# Data Engineering Project - Cold Drinks Data Pipeline

## 📌 Overview
This repository contains an **ETL pipeline** built using **Apache Airflow** and executed within **WSL (Windows Subsystem for Linux)**. The pipeline is designed to extract, transform, and analyze **Cold Drinks Market Data**, providing insights into consumer behavior and market trends.

## 🚀 Project Workflow
1. **Data Extraction**: Loads raw data from multiple CSV files in a directory.
2. **Data Transformation**: Performs cleaning, data type conversion, and various analyses.
3. **Data Loading**: Stores processed results into structured files.
4. **Automated Execution**: The pipeline runs on **Apache Airflow**, ensuring scheduled execution.

## 📁 Project Structure
📂 Data-Engineering-Project │-- 📄 README.md (This file) │-- 📂 Data │ │-- Processed_Cold_Drinks_Data.csv (Processed data output) │-- 📂 Scripts │ │-- etl_dag.py (Airflow DAG for ETL process) │ │-- etl_script.py (ETL logic implementation) │ │-- wrapper_script.sh (Shell script to trigger ETL execution)

markdown
Copy
Edit

## 🛠️ Technologies Used
- **Apache Airflow** - Workflow orchestration
- **Python (pandas, matplotlib)** - Data processing and visualization
- **WSL (Windows Subsystem for Linux)** - Execution environment
- **Bash (Shell Scripting)** - Automating script execution

## 📊 ETL Pipeline Components

### 1️⃣ **Airflow DAG (etl_dag.py)**
Defines an **ETL workflow** using Airflow, scheduling tasks for data extraction, transformation, and analysis.

### 2️⃣ **ETL Script (etl_script.py)**
Contains functions for:
- **Loading data** from multiple CSVs
- **Analyzing Age vs Frequency** of consumption
- **Identifying effective marketing channels** by age group
- **Understanding packaging preferences** for health-conscious consumers
- **Examining taste ratings vs price range**
- **Analyzing urban vs rural barriers** to trying new brands

### 3️⃣ **Wrapper Script (wrapper_script.sh)**
Executes the **ETL pipeline** using a shell script in **WSL**.

## 🔄 How to Run the Project
1. **Set up Apache Airflow**:
   ```bash
   pip install apache-airflow
   airflow db init
   airflow webserver -p 8080 &
   airflow scheduler &
Place input data in ./airflow/input_data/.
Run the DAG in Airflow UI (http://localhost:8080).
Trigger ETL manually (if needed):
bash
Copy
Edit
bash wrapper_script.sh
📈 Output
Processed CSV: Cleaned and structured dataset.
Graphs & Insights: Saved as images (.png) in ./airflow/extract_folder/.
Aggregated Reports: Saved as CSV files for analysis.
