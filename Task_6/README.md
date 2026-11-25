# Connect MySQL Database & Exploratory Data Analysis: UCI Wine Quality

[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1.svg?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.1+-D71F00.svg?style=flat&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557c.svg?style=flat)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-388e3c.svg?style=flat)](https://seaborn.pydata.org/)

An end-to-end data pipeline demonstrating how to connect Python to a **MySQL relational database**, create schemas, ingest real-world public data from the **UCI Machine Learning Repository**, execute SQL queries using `pandas.read_sql`, and produce statistical visualizations.

---

## 📌 Dataset Source & Attribution

- **Dataset Name:** Wine Quality (Red) Dataset
- **Repository:** [UCI Machine Learning Repository — Wine Quality Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Direct Data URL:** [https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
- **Citation:** Cortez et al., 2009 (*Modeling wine preferences by data mining from physicochemical properties*).
- **Attributes:**
  - `fixed_acidity`: Tartaric acid concentration ($g/dm^3$)
  - `volatile_acidity`: Acetic acid concentration ($g/dm^3$)
  - `citric_acid`: Citric acid concentration ($g/dm^3$)
  - `residual_sugar`: Sugar remaining after fermentation stops ($g/dm^3$)
  - `chlorides`: Amount of salt in wine ($g/dm^3$)
  - `free_sulfur_dioxide` & `total_sulfur_dioxide`: $SO_2$ preventing microbial growth ($mg/dm^3$)
  - `density`: Density of water/alcohol/sugar mixture ($g/cm^3$)
  - `pH`: Acidity level (scale from 0 to 14)
  - `sulphates`: Potassium sulphate additive ($g/dm^3$)
  - `alcohol`: Percent alcohol content (% by volume)
  - `quality`: Sensory evaluation score (target metric between 0 and 10)
- **Total Records:** 1,599 instances with 0 missing values.

---

## 📓 Interactive Notebook (Outputs Visible)

The complete executed Jupyter notebook with all SQL executions, printed dataframes, summary statistics, and rendered charts is available directly at:  
👉 **[View Notebook: `connect_mysql_database.ipynb`](connect_mysql_database.ipynb)**

---

## 🗂️ Project Structure

```text
Connect-MySQL-database/
├── .gitignore                              # Git ignore rules for Python & Jupyter
├── README.md                               # Project documentation and summary
├── requirements.txt                        # Project dependencies
├── chart1_alcohol_by_quality.png           # Exported Chart 1 (Bar & trend plot)
├── chart2_volatile_acidity_vs_alcohol.png  # Exported Chart 2 (Scatter plot)
├── data/
│   └── winequality-red.csv                 # Local copy of UCI Wine Quality dataset
└── connect_mysql_database.ipynb            # Executed Jupyter notebook with outputs visible
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/godwintharun3-source/Connect-MySQL-database.git
cd Connect-MySQL-database
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure MySQL Database
Make sure your MySQL server is running (default credentials: `root:root` on `localhost:3306` or set via environment variables):
```bash
export MYSQL_HOST="localhost"
export MYSQL_USER="root"
export MYSQL_PASSWORD="your_password"
export MYSQL_PORT="3306"
```

### 4. Launch the Jupyter Notebook
```bash
jupyter notebook connect_mysql_database.ipynb
```

---

## 💻 Code Walkthrough & SQL Outputs

### 1. MySQL Connection & Schema Creation
```python
import pymysql
from sqlalchemy import create_engine
import pandas as pd

# Connect to MySQL and create database
conn = pymysql.connect(host="localhost", user="root", password="root", port=3306)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS wine_analytics;")
conn.commit()
conn.close()

# SQLAlchemy connection engine
engine = create_engine("mysql+pymysql://root:root@localhost:3306/wine_analytics")
```

---

### 2. Data Ingestion into MySQL Table
```python
df = pd.read_csv("data/winequality-red.csv")
df.to_sql(name="wine_quality", con=engine, if_exists="replace", index=False)
```

---

### 3. Direct SQL Aggregation via Pandas
```sql
SELECT 
    quality,
    COUNT(*) AS sample_count,
    ROUND(AVG(alcohol), 2) AS avg_alcohol,
    ROUND(AVG(volatile_acidity), 2) AS avg_volatile_acidity,
    ROUND(AVG(citric_acid), 2) AS avg_citric_acid,
    ROUND(AVG(sulphates), 2) AS avg_sulphates
FROM wine_quality
GROUP BY quality
ORDER BY quality DESC;
```

**SQL Output:**
| quality | sample_count | avg_alcohol | avg_volatile_acidity | avg_citric_acid | avg_sulphates |
|:-------:|:------------:|:-----------:|:--------------------:|:---------------:|:-------------:|
| **8** | 18 | **12.09%** | **0.42** | 0.39 | 0.77 |
| **7** | 199 | **11.47%** | **0.40** | 0.38 | 0.74 |
| **6** | 638 | 10.63% | 0.50 | 0.27 | 0.68 |
| **5** | 681 | 9.90% | 0.58 | 0.24 | 0.62 |
| **4** | 53 | 10.27% | 0.69 | 0.17 | 0.60 |
| **3** | 10 | **9.96%** | **0.88** | 0.17 | 0.57 |

---

### 4. SQL Segmentation by Quality Tier (`CASE WHEN`)
```sql
SELECT 
    CASE 
        WHEN quality >= 7 THEN 'High Quality (7-8)'
        WHEN quality >= 5 THEN 'Medium Quality (5-6)'
        ELSE 'Low Quality (3-4)'
    END AS quality_tier,
    COUNT(*) AS total_samples,
    ROUND(AVG(alcohol), 2) AS mean_alcohol,
    ROUND(AVG(volatile_acidity), 2) AS mean_volatile_acidity,
    ROUND(AVG(pH), 2) AS mean_ph
FROM wine_quality
GROUP BY quality_tier
ORDER BY mean_alcohol DESC;
```

**SQL Output:**
| quality_tier | total_samples | mean_alcohol | mean_volatile_acidity | mean_ph |
|:---|:---:|:---:|:---:|:---:|
| **High Quality (7-8)** | 217 | **11.52%** | **0.41** | 3.29 |
| **Medium Quality (5-6)** | 1,319 | 10.25% | 0.54 | 3.31 |
| **Low Quality (3-4)** | 63 | 10.22% | **0.72** | 3.40 |

---

## 📊 Visualizations

### Chart 1: Alcohol Content by Wine Quality Rating
![Chart 1: Alcohol Content by Wine Quality Rating](chart1_alcohol_by_quality.png)

### Chart 2: Volatile Acidity vs. Alcohol Content across Quality Tiers
![Chart 2: Volatile Acidity vs. Alcohol Content](chart2_volatile_acidity_vs_alcohol.png)

---

## 🔍 Key Findings in Plain Words

1. **Alcohol is the Strongest Positive Predictor of Wine Quality ($r = 0.476$):**
   - Higher-quality red wines (scores 7 and 8) have significantly higher alcohol content, averaging **11.47% to 12.09%**.
   - In contrast, mediocre and low-quality wines (scores 3 through 5) cluster around **9.9% to 10.3%**.
   - As visualized in Chart 1, wine quality scores show a consistent upward stair-step pattern corresponding with higher alcohol concentration.

2. **Volatile Acidity (Acetic Acid) Strongly Degrades Quality ($r = -0.391$):**
   - Volatile acidity measures the presence of acetic acid, which gives wine an unpleasant, sour vinegar taste when elevated.
   - Low-quality wines (rating 3) exhibit high volatile acidity averaging **0.88 g/dm³**, whereas top-rated wines (rating 8) maintain low volatile acidity averaging **0.42 g/dm³**—less than half the amount.
   - As seen in Chart 2, high-quality wines (green points) distinctly occupy the lower-right quadrant: **high alcohol combined with low volatile acidity**.

3. **Database Processing Efficiency:**
   - Loading the dataset into MySQL and executing aggregations via SQL (`GROUP BY` and `CASE WHEN`) allowed rapid summarization across 1,599 records directly in the database engine, streamlining analytical queries for Python and Pandas.

---

## 👤 Author
- **Name:** Tharun Godwin C
- **GitHub:** [@godwintharun3-source](https://github.com/godwintharun3-source)
- **Repository:** [Connect-MySQL-database](https://github.com/godwintharun3-source/Connect-MySQL-database)
