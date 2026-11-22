import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from nbclient import NotebookClient

# Ensure required directories exist
os.makedirs("dataset", exist_ok=True)
os.makedirs("notebooks", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Initialize notebook
nb = new_notebook(metadata={
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "name": "python",
        "version": "3.12"
    }
})

# Cell 1: Title & Overview
cell1_md = """# 🚢 Exploratory Data Analysis & CSV Ingestion: Titanic Passenger Dataset

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/godwintharun3-source/Import-CSV-files/blob/main/notebooks/titanic_csv_import_analysis.ipynb)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-CSV%20Import-150458?logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualizations-4C72B0)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)

**Source:** [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)  
**Dataset Format:** Comma-Separated Values (`.csv`)  
**Author:** Tharun Godwin  
**Environment:** Python 3 (pandas, NumPy, Matplotlib, Seaborn)  

---

### 📌 Project Overview
This notebook presents a comprehensive study of data ingestion, manipulation, and exploratory analysis using the **pandas** library in Python:
1. **Core Pandas Concepts**: Demonstrating the difference between a 1D `Series` and a 2D `DataFrame`.
2. **Tabular Data Creation**: Creating DataFrames from Python dictionaries: `pd.DataFrame({"name": [...], "marks": [...]})`.
3. **CSV Ingestion**: Ingesting real-world tabular data using `pd.read_csv()`.
4. **Data Inspection**: Auditing structural integrity and statistics via `head()`, `shape`, `info()`, and `describe()`.
5. **Exploratory Analytics**: Grouping and slicing data to uncover behavioral patterns.
6. **Data Visualization**: Building publication-grade figures with **Matplotlib** and **Seaborn**.
7. **Plain-Language Findings**: Translating quantitative metrics into clear, intuitive insights.
"""

# Cell 2: Concept 1 Markdown
cell2_md = """## 1. Core Pandas Concepts: Series vs. DataFrame

**"Pandas gives labelled tables for data analysis."**

A helpful mental model: **A DataFrame is an Excel sheet you can command with Python.**

| Concept | Structure | Dimensions | Analogy | Code Example |
|---|---|---|---|---|
| **Series** | Labelled 1D array | 1 Dimension | A single labelled spreadsheet column | `pd.Series([85, 92, 78], name="marks")` |
| **DataFrame** | 2D labelled tabular structure | 2 Dimensions | An entire multi-column Excel spreadsheet | `pd.DataFrame({"name": [...], "marks": [...]})` |

Let's begin by importing our libraries and creating sample Series and DataFrames from scratch.
"""

# Cell 3: Setup & Scratch Creation Code
cell3_code = """import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

# Set publication styling
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.labelsize"] = 12

print("=== Library Versions ===")
print(f"Pandas     : {pd.__version__}")
print(f"NumPy      : {np.__version__}")
print(f"Matplotlib : {plt.matplotlib.__version__}")
print(f"Seaborn    : {sns.__version__}")
print("========================\\n")

# 1. Create a Series (1D labelled column)
marks_series = pd.Series([85, 92, 78, 95], index=["Alice", "Bob", "Charlie", "Diana"], name="Marks")
print("--- 1. Pandas Series Example ---")
print(marks_series)
print(f"Series Type: {type(marks_series)}, Dimensions: {marks_series.ndim}, Shape: {marks_series.shape}\\n")

# 2. Create a DataFrame (2D labelled table)
students_df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "marks": [88, 92, 79, 95],
    "grade": ["A", "A+", "B+", "O"]
})
print("--- 2. Pandas DataFrame Example ---")
print(students_df)
print(f"DataFrame Type: {type(students_df)}, Dimensions: {students_df.ndim}, Shape: {students_df.shape}")
"""

# Cell 4: File Ingestion Overview Markdown
cell4_md = """## 2. Reading External Data in Pandas

Pandas provides optimized readers for virtually every structured file format:
- `pd.read_csv()`: Parses delimited text files (`.csv`, `.tsv`, `.txt`). Handles separators (`sep=','` or `sep=';'`), encodings, and missing value indicators.
- `pd.read_excel()`: Ingests Microsoft Excel workbooks (`.xlsx`, `.xls`) with multiple sheets.
- `pd.read_json()`: Reads JavaScript Object Notation (`.json`) files and API responses.
- `pd.read_sql()`: Connects directly to relational databases via SQL queries.

In this project, we ingest the public **Titanic Passenger Dataset** stored in CSV format.
"""

# Cell 5: Dataset Source & Ingestion Code
cell5_code = """# Define dataset path
csv_file_path = "dataset/titanic.csv"

# Colab / standalone fallback to ensure reproducibility
if not os.path.exists(csv_file_path):
    os.makedirs("dataset", exist_ok=True)
    import urllib.request
    dataset_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    urllib.request.urlretrieve(dataset_url, csv_file_path)
    print(f"Downloaded dataset from repository to: {csv_file_path}")

# Ingest CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)
print(f"Successfully loaded '{csv_file_path}' into a pandas DataFrame.")
print(f"Dataset Dimensions: {df.shape[0]} rows (passengers) x {df.shape[1]} columns (features)\\n")

# Preview the first 5 records
df.head()
"""

# Cell 6: Inspecting DataFrame Markdown
cell6_md = """## 3. Inspecting the DataFrame

Once data is loaded into memory, four essential inspection methods provide instant visibility into its structure and quality:
1. `head(n)` & `tail(n)`: Display the first and last $n$ rows.
2. `shape`: A tuple `(rows, columns)` reporting total dimensions.
3. `info()`: Comprehensive structural overview — column names, non-null counts, data types (`int64`, `float64`, `object`), and memory usage.
4. `describe()`: Quantitative statistical summary — count, mean, standard deviation, minimum, 25th percentile, median (50%), 75th percentile, and maximum.
"""

# Cell 7: Inspection Code Part 1
cell7_code = """print("=== First 5 Records (df.head()) ===")
display(df.head(5))

print("\\n=== Last 5 Records (df.tail()) ===")
display(df.tail(5))

print(f"\\n=== Dataset Shape: {df.shape} ===")
print(f"Total Rows (Instances): {df.shape[0]}")
print(f"Total Columns (Features): {df.shape[1]}")

print("\\n=== DataFrame Info (df.info()) ===")
df.info()
"""

# Cell 8: Inspection Code Part 2 (describe & missing values)
cell8_code = """print("=== Numerical Feature Statistics (df.describe()) ===")
display(df.describe().round(2))

print("\\n=== Categorical Feature Statistics (df.describe(include=['object'])) ===")
display(df.describe(include=['object']))

print("\\n=== Missing Value Audit (df.isnull().sum()) ===")
missing_df = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage (%)": (df.isnull().sum() / len(df) * 100).round(2)
})
display(missing_df[missing_df["Missing Count"] > 0])
"""

# Cell 9: Grouping & Aggregations Markdown
cell9_md = """## 4. Slicing, Indexing & Grouped Aggregations

Using pandas indexing and `.groupby()`, we can interrogate the dataset to answer targeted analytical questions:
- What percentage of passengers survived overall?
- Did passenger gender affect survival rates?
- Did socioeconomic class (`Pclass`) determine survival probability?
- What was the financial disparity in fares between those who survived and those who perished?
"""

# Cell 10: Grouping Code
cell10_code = """# Overall Survival Rate
overall_survival = df["Survived"].mean() * 100
print(f"Overall Passenger Survival Rate: {overall_survival:.2f}%\\n")

# 1. Survival Rate by Gender (Sex)
gender_survival = df.groupby("Sex")["Survived"].agg(
    Total="count",
    Survived="sum",
    Survival_Rate=lambda x: round(x.mean() * 100, 2)
)
print("=== Survival Breakdown by Gender ===")
display(gender_survival)

# 2. Survival Rate by Socioeconomic Class (Pclass)
class_survival = df.groupby("Pclass")["Survived"].agg(
    Total="count",
    Survived="sum",
    Survival_Rate=lambda x: round(x.mean() * 100, 2),
    Avg_Fare=lambda x: round(df.loc[x.index, "Fare"].mean(), 2)
)
print("\\n=== Survival Breakdown by Passenger Class ===")
display(class_survival)

# 3. Intersectional Analysis: Class and Gender
intersectional = df.groupby(["Pclass", "Sex"])["Survived"].agg(
    Total="count",
    Survived="sum",
    Survival_Rate=lambda x: round(x.mean() * 100, 2)
).unstack()
print("\\n=== Intersectional Survival Rate (%) by Class & Gender ===")
display(intersectional["Survival_Rate"])

# 4. Financial Disparity: Fare Paid by Survival Status
fare_summary = df.groupby("Survived")["Fare"].agg(
    Count="count",
    Mean_Fare="mean",
    Median_Fare="median",
    Std_Fare="std",
    Max_Fare="max"
).round(2)
fare_summary.index = ["Perished (0)", "Survived (1)"]
print("\\n=== Fare Statistics by Survival Outcome ===")
display(fare_summary)
"""

# Cell 11: Visualizations Section Markdown
cell11_md = """## 5. Visualizations with Matplotlib & Seaborn

We now create three clear, publication-quality visualizations to communicate the empirical findings:
1. **Chart 1: Survival Rate Across Passenger Classes Segmented by Gender** (Grouped Bar Chart).
2. **Chart 2: Ticket Fare Distribution by Survival Status** (Boxplot with Jittered Strip Plot).
3. **Chart 3: Age Demographics and Survival Distribution** (KDE Distribution Curves).
"""

# Cell 12: Chart 1 Code
cell12_code = """# Chart 1: Survival Rate Across Passenger Classes Segmented by Gender
plt.figure(figsize=(10, 6))

# Calculate rates for plotting
rate_data = df.groupby(["Pclass", "Sex"])["Survived"].mean().reset_index()
rate_data["Survival_Rate_Pct"] = rate_data["Survived"] * 100
rate_data["Class_Label"] = rate_data["Pclass"].map({1: "1st Class", 2: "2nd Class", 3: "3rd Class"})

ax = sns.barplot(
    data=rate_data,
    x="Class_Label",
    y="Survival_Rate_Pct",
    hue="Sex",
    palette={"female": "#e74c3c", "male": "#2980b9"},
    edgecolor="black",
    linewidth=1.2,
    alpha=0.9
)

# Annotate each bar with the percentage
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        ax.annotate(
            f"{height:.1f}%",
            (p.get_x() + p.get_width() / 2., height),
            ha='center', va='bottom',
            fontsize=12, fontweight='bold',
            xytext=(0, 4), textcoords='offset points'
        )

plt.title("Chart 1: Passenger Survival Rate by Socioeconomic Class & Gender", pad=15)
plt.xlabel("Passenger Class", labelpad=10)
plt.ylabel("Survival Rate (%)", labelpad=10)
plt.ylim(0, 110)
plt.legend(title="Gender", labels=["Female", "Male"], loc="upper right")
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/chart1_survival_by_class_and_gender.png", dpi=300)
plt.show()
"""

# Cell 13: Chart 2 Code
cell13_code = """# Chart 2: Ticket Fare Distribution by Survival Status
plt.figure(figsize=(10, 6))

# Cap extreme fare outlier at 300 for optimal visualization clarity
plot_df = df.copy()
plot_df["Fare_Capped"] = plot_df["Fare"].clip(upper=300)
plot_df["Outcome"] = plot_df["Survived"].map({0: "Perished (0)", 1: "Survived (1)"})

palette = {"Perished (0)": "#e74c3c", "Survived (1)": "#2ecc71"}

ax = sns.boxplot(
    data=plot_df,
    x="Outcome",
    y="Fare_Capped",
    palette=palette,
    width=0.45,
    fliersize=3,
    linewidth=1.5,
    showmeans=True,
    meanprops={"marker": "D", "markerfacecolor": "yellow", "markeredgecolor": "black", "markersize": 8}
)

# Overlay individual observations with a strip plot
sns.stripplot(
    data=plot_df,
    x="Outcome",
    y="Fare_Capped",
    color="black",
    alpha=0.2,
    jitter=0.2,
    size=3
)

# Add annotations for median and mean
perished_median = df[df["Survived"] == 0]["Fare"].median()
perished_mean = df[df["Survived"] == 0]["Fare"].mean()
survived_median = df[df["Survived"] == 1]["Fare"].median()
survived_mean = df[df["Survived"] == 1]["Fare"].mean()

ax.text(0, perished_median + 8, f"Median: ${perished_median:.2f}\\nMean: ${perished_mean:.2f}",
        ha="center", bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#e74c3c", lw=1.2), fontsize=10, fontweight="bold")

ax.text(1, survived_median + 15, f"Median: ${survived_median:.2f}\\nMean: ${survived_mean:.2f}",
        ha="center", bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#2ecc71", lw=1.2), fontsize=10, fontweight="bold")

plt.title("Chart 2: Ticket Fare Distribution of Passengers by Survival Outcome", pad=15)
plt.xlabel("Survival Status", labelpad=10)
plt.ylabel("Fare Paid in British Pounds (£) [Capped at £300]", labelpad=10)

# Custom legend for diamond mean marker
plt.plot([], [], marker='D', color='yellow', markeredgecolor='black', linestyle='None', markersize=8, label='Mean Fare')
plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig("images/chart2_fare_distribution_by_survival.png", dpi=300)
plt.show()
"""

# Cell 14: Chart 3 Code
cell14_code = """# Chart 3: Age Distribution & Passenger Survival Demographics
plt.figure(figsize=(10, 6))

sns.kdeplot(
    data=df[df["Survived"] == 0]["Age"].dropna(),
    label="Perished (0)",
    color="#e74c3c",
    fill=True,
    alpha=0.35,
    linewidth=2.5
)

sns.kdeplot(
    data=df[df["Survived"] == 1]["Age"].dropna(),
    label="Survived (1)",
    color="#27ae60",
    fill=True,
    alpha=0.35,
    linewidth=2.5
)

# Vertical line for median age
median_age = df["Age"].median()
plt.axvline(median_age, color="navy", linestyle="--", linewidth=1.5, label=f"Median Age ({median_age:.0f} yrs)")

# Annotate children survival peak
plt.annotate(
    "Elevated survival peak\\nfor children (< 10 yrs)",
    xy=(4, 0.022),
    xytext=(15, 0.030),
    arrowprops=dict(facecolor="black", shrink=0.08, width=1.5, headwidth=8),
    fontsize=11,
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.4", fc="#fff8dc", ec="#f39c12", lw=1.2)
)

plt.title("Chart 3: Kernel Density Estimate (KDE) of Age by Survival Outcome", pad=15)
plt.xlabel("Passenger Age (Years)", labelpad=10)
plt.ylabel("Probability Density", labelpad=10)
plt.xlim(0, 85)
plt.legend(loc="upper right", frameon=True)

plt.tight_layout()
plt.savefig("images/chart3_age_survival_distribution.png", dpi=300)
plt.show()
"""

# Cell 15: Plain Language Findings Markdown
cell15_md = """## 6. Key Findings in Plain Words

Through our exploratory data analysis of the Titanic passenger dataset using pandas, here is what the empirical numbers reveal in clear, plain language:

### 1. Gender was the Decisive Factor in Survival
- Overall, only **38.38%** of passengers survived the disaster.
- However, **74.20% of all female passengers survived**, compared to just **18.89% of male passengers**.
- This directly reflects the maritime evacuation protocol ("women and children first").

### 2. Social Class Dictated Evacuation Priority
- Passengers in **1st Class** had a **62.96%** survival rate.
- Passengers in **2nd Class** had a **47.28%** survival rate.
- Passengers in **3rd Class (Steerage)** had only a **24.24%** survival rate.
- Lower deck cabin placement, greater physical distance to the boat deck, and socioeconomic bias resulted in over 75% of steerage passengers losing their lives.

### 3. The Intersectional Divide: 1st Class Women vs. 3rd Class Men
- An astonishing **96.81% of 1st Class women** survived (91 out of 94).
- In stark contrast, only **13.54% of 3rd Class men** survived (47 out of 347).
- A first-class woman was more than **7 times more likely** to survive than a third-class man.

### 4. Economic Wealth Afforded Better Odds
- Survivors paid an average ticket fare of **£48.40** (median **£26.00**), whereas non-survivors paid an average of **£22.12** (median **£10.50**).
- Passengers paying over £50 were disproportionately accommodated on upper promenade decks with direct life-raft access.

### 5. Children Received Evacuation Priority
- The age density curve shows a pronounced survival spike for young children under **10 years old** (~61% survival rate for children aged 0–9), affirming that youth priority was honored during lifeboat boarding.
"""

# Cell 16: Reflection / What I Did and What I Learned Markdown
cell16_md = """## 7. Summary: What I Did and What I Learned

### What I Did:
1. **Configured Environment**: Set up pandas, NumPy, Matplotlib, and Seaborn with consistent themes and parameters.
2. **Practiced Core Fundamentals**: Created individual pandas `Series` and multi-column `DataFrames` using Python dictionaries (`pd.DataFrame({"name": [...], "marks": [...]})`).
3. **Ingested Real-World CSV Data**: Ingested the public Kaggle Titanic dataset using `pd.read_csv()` with automated fallback paths.
4. **Inspected Dataset Structure**: Applied `head()`, `tail()`, `shape`, `info()`, and `describe()` to audit dimensions, missing entries (e.g., `Age` and `Cabin`), and numeric distributions.
5. **Performed Grouped Queries**: Leveraged `.groupby()` to calculate survival statistics across gender, socioeconomic class, and fare brackets.
6. **Produced Publication Visualizations**: Generated three high-resolution charts depicting categorical survival rates, fare distributions, and age demographics.
7. **Documented Discoveries**: Articulated data-driven conclusions in plain, unambiguous prose.

### What I Learned (In My Own Words):
- **A DataFrame is truly an interactive spreadsheet powered by Python**: Unlike static spreadsheets, pandas allows seamless automation, programmatic reproducibility, and vectorized mathematical operations on millions of rows in milliseconds.
- **Series vs. DataFrame Distinction**: A `Series` is a single labelled 1D array representing one column, while a `DataFrame` is a full 2D table combining multiple Series that share a common index.
- **Data Inspection Saves Time**: Running `.info()` and `.isnull().sum()` immediately highlights data quality problems (like missing ages or missing cabins) before running statistical models.
- **Summary Statistics (`describe()`) Reveal Skewness**: Comparing the mean fare (£32.20) to the median fare (£14.45) instantly revealed heavy positive skewness driven by a handful of ultra-wealthy ticket holders.
- **Pandas `.groupby()` is the Ultimate Data Aggregation Tool**: Slicing across multiple categorical variables (such as `Pclass` and `Sex`) allows complex business and demographic insights to be computed in a single readable line of code.
"""

# Assemble all cells
nb.cells = [
    new_markdown_cell(cell1_md),
    new_markdown_cell(cell2_md),
    new_code_cell(cell3_code),
    new_markdown_cell(cell4_md),
    new_code_cell(cell5_code),
    new_markdown_cell(cell6_md),
    new_code_cell(cell7_code),
    new_code_cell(cell8_code),
    new_markdown_cell(cell9_md),
    new_code_cell(cell10_code),
    new_markdown_cell(cell11_md),
    new_code_cell(cell12_code),
    new_code_cell(cell13_code),
    new_code_cell(cell14_code),
    new_markdown_cell(cell15_md),
    new_markdown_cell(cell16_md)
]

print(f"Total cells assembled: {len(nb.cells)}")

# Execute notebook using NotebookClient
print("Executing notebook via NotebookClient...")
client = NotebookClient(nb, timeout=120, kernel_name="python3")
client.execute()
print("Execution completed successfully!")

# Save notebook with executed outputs
notebook_output_file = "notebooks/titanic_csv_import_analysis.ipynb"
with open(notebook_output_file, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Executed notebook saved to: {notebook_output_file}")
