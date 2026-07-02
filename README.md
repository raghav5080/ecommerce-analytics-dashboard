# E-Commerce Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![SQL](https://img.shields.io/badge/SQL-SQLite-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## Business Problem

Analysed **500,000+ rows** of real UK e-commerce transaction data (UCI Online Retail Dataset)
to answer 5 key business questions about revenue performance, customer behaviour,
and product trends — simulating the kind of analysis a Data Analyst would deliver
to a business stakeholder.

---

## Business Questions Answered

1. Which countries generate the most revenue?
2. What are the top-selling products by volume?
3. How has monthly revenue trended over time?
4. When (day and hour) do customers spend the most?
5. How many unique customers are active each month?

---

## Key Findings

- **UK accounts for 84% of total revenue**, making it the dominant market by a significant margin
- **PAPER CRAFT , LITTLE BIRDIE** was the highest-selling item with **80995** across the period
- **Revenue peaked in **November 2011** and showed a notable dip in **Feburary 2011**
- **Friday night (9:00 PM - 10:00 PM)** show the highest transaction volume across the week
- Monthly unique active customers ranged from **615** to **1664**, with growth visible in Q4

---

## Project Structure

```
ecommerce-analytics-dashboard/
│
├── ecommerce_analysis.ipynb     ← Full analysis notebook (cleaning + EDA + SQL + charts)
├── cleaned_retail.csv           ← Cleaned dataset after preprocessing
├── ecommerce.db                 ← SQLite database used for SQL queries
├── requirements.txt             ← Python libraries needed to run the notebook
├── README.md                    ← This file
│
└── charts/                      ← Exported chart images
    ├── monthly_revenue.png
    ├── country_revenue.png
    ├── top_products.png
    └── heatmap.png
```

---

## Tools & Technologies

| Category        | Tool / Library                        |
|-----------------|---------------------------------------|
| Language        | Python 3.x                            |
| Data Analysis   | Pandas, NumPy                         |
| Visualisation   | Matplotlib, Seaborn                   |
| Database        | SQLite (via Python sqlite3 module)    |
| Dashboard       | Google Looker Studio                  |
| Environment     | Jupyter Notebook                      |
| Version Control | Git, GitHub                           |

---

## Data Source

**UCI Online Retail Dataset** — publicly available on Kaggle.
Contains transactional data from a UK-based online retailer between 2010 and 2011.

- **Rows:** ~541,000 (raw) → ~397,000 (after cleaning)
- **Columns:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

---

## How to Run This Project Locally

**1. Clone the repository**
```bash
git clone https://github.com/raghav5080/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Launch Jupyter Notebook**
```bash
jupyter notebook
```

**4. Open** `ecommerce_analysis_celan.ipynb` and run all cells top to bottom.

> Note: The raw dataset (`online_retail.csv`) is not included due to file size.
> Download it from [Kaggle — E-Commerce Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
> and place it in the root folder before running.

---

## Data Cleaning Steps Performed

- Removed rows with null `CustomerID` (no customer = no retention analysis possible)
- Removed rows with negative `Quantity` (cancellations and returns)
- Removed rows with zero `UnitPrice` (data errors / free items)
- Converted `InvoiceDate` from string to datetime format
- Created derived column `TotalPrice = Quantity × UnitPrice`
- Extracted `Month`, `DayOfWeek`, and `Hour` from `InvoiceDate` for time-based analysis

---

## SQL Queries Used

All queries were run against a local SQLite database created from the cleaned dataframe.
Key patterns covered:

- `GROUP BY` with `SUM()` and `COUNT(DISTINCT ...)`
- Date extraction using `strftime()`
- `HAVING` clause for multi-month customer filtering
- Subqueries for order-level aggregation

---

## Author

**Raghav Dixit**
Data Analyst | Bengaluru, India
[LinkedIn](https://www.linkedin.com/in/raghavdixit-5776451a5) · [GitHub](https://github.com/raghav5080)

---

*This project was built as part of a data analytics portfolio to demonstrate
end-to-end analysis skills: data cleaning, exploratory analysis, SQL querying,
visualisation, and business dashboarding.*
