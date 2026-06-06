# Expense Tracker with Data Visualization

## Project Overview

Expense Tracker is a Python-based data analysis project developed to monitor, analyze, and visualize personal expense data. The application processes expense records from CSV files, performs statistical analysis, generates graphical visualizations, and exports summarized reports to Excel format.

The project demonstrates practical implementation of data analysis, report automation, and visualization techniques using Python libraries.

---

## Features

* Read and process expense records from CSV files
* Perform category-wise expense analysis
* Generate statistical summaries of expenses
* Create visual reports using charts
* Monitor spending trends over time
* Export analyzed reports to Excel format
* Organize generated charts and reports automatically

---

## Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Programming Language         |
| Pandas     | Data Analysis and Processing |
| Matplotlib | Data Visualization           |
| OpenPyXL   | Excel Report Generation      |

---

## Project Structure

```text
Expense_Tracker/
│
├── data/
│   └── expenses.csv
│
├── charts/
│   ├── pie.png
│   ├── bar.png
│   └── trend.png
│
├── reports/
│   └── Expense_Report.xlsx
│
├── main.py
└── README.md
```

---

## Installation

Install the required libraries before running the project.

```bash
pip install pandas matplotlib openpyxl
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-internship-projects.git
```

2. Navigate to the project directory:

```bash
cd Expense_Tracker
```

3. Ensure the dataset is available:

```text
data/expenses.csv
```

4. Run the application:

```bash
python main.py
```

---

## Input Dataset

The project uses a CSV dataset containing expense information.

Example:

```csv
Date,Category,Description,Amount,Payment_Mode
2026-01-01,Food,Restaurant Bill,850,UPI
2026-01-02,Transport,Metro Recharge,200,Card
2026-01-03,Bills,Electricity Bill,2400,Net Banking
```

---

## Statistical Analysis

The application calculates:

* Total Expense
* Average Expense
* Highest Expense
* Lowest Expense
* Category-wise Expense Summary
* Daily Expense Trend

---

## Generated Visualizations

### Pie Chart

Displays percentage-wise expense distribution across categories.

Output:

```text
charts/pie.png
```

### Bar Chart

Displays category-wise expense comparison.

Output:

```text
charts/bar.png
```

### Trend Chart

Displays expense trends over time.

Output:

```text
charts/trend.png
```

---

## Excel Report

The application generates an Excel report automatically:

```text
reports/Expense_Report.xlsx
```

The report contains:

### Sheet 1 - Raw Data

Original expense records from the dataset.

### Sheet 2 - Summary

Statistical analysis results including total, average, minimum, and maximum expenses.

### Sheet 3 - Category Summary

Category-wise expense breakdown and visual analysis.

---

## Learning Outcomes

This project demonstrates:

* Data preprocessing using Pandas
* Expense analysis and aggregation
* Data visualization using Matplotlib
* Automated Excel report generation
* File handling and directory management
* Practical implementation of financial data analysis

* Database integration
* Multi-user expense management

---
This project is intended for educational and learning purposes.
