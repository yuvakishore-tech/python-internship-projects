# Excel Report Generator with Data Analysis

## Project Overview

Excel Report Generator is a Python-based automation project developed to generate structured Excel reports from CSV datasets. The application reads and processes CSV data, performs statistical analysis, creates pivot tables, generates visual charts, and exports formatted Excel reports automatically.

The project demonstrates practical implementation of data processing, report automation, and visualization techniques using Python libraries.

---

## Features

* Read and process CSV datasets
* Perform statistical analysis on numeric data
* Generate summary reports automatically
* Create pivot table analysis
* Generate visual charts for data representation
* Export formatted Excel reports
* Automate Excel report generation workflow

---

## Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Programming Language         |
| Pandas     | Data Analysis and Processing |
| Matplotlib | Data Visualization           |
| OpenPyXL   | Excel File Generation        |
| Tkinter    | Graphical User Interface     |

---

## Project Structure

```text id="w98b4h"
Excel_report_generator/
│
├── main.py
├── sample.csv
├── report.xlsx
├── project_explanation.txt
└── README.md
```

---

## Installation

Install the required libraries before running the project.

```bash id="rtxogd"
pip install pandas matplotlib openpyxl
```

---

## How to Run

1. Clone the repository:

```bash id="rvl0h5"
git clone https://github.com/your-username/python-internship-projects.git
```

2. Navigate to the project directory:

```bash id="bxwjlwm"
cd Excel_report_generator
```

3. Ensure the dataset is available:

```text id="q0ejc8"
sample.csv
```

4. Run the application:

```bash id="9oy8rt"
python main.py
```

5. Upload the CSV file using the graphical interface and save the generated Excel report.

---

## Input Dataset

The project uses a CSV dataset containing structured data records.

Example:

```csv id="3njd4u"
Category,Amount,Date
Food,250,2026-01-01
Travel,500,2026-01-02
Shopping,1200,2026-01-03
```

---

## Statistical Analysis

The application calculates:

* Total Value
* Average Value
* Minimum Value
* Maximum Value
* Category-wise Aggregation
* Pivot Table Analysis

---

## Generated Visualizations

### Bar Chart

Displays category-wise data comparison.

Generated Output:

```text id="w0l5xs"
Embedded directly into the Excel report
```

---

## Excel Report

The application generates a formatted Excel report automatically:

```text id="6jl3b5"
report.xlsx
```

The report contains:

### Sheet 1 - Raw Data

Original dataset records from the CSV file.

### Sheet 2 - Summary

Statistical analysis results including total, average, minimum, and maximum values.

### Sheet 3 - Pivot Table

Category-wise aggregated analysis with chart visualization.

---

## Learning Outcomes

This project demonstrates:

* CSV file handling using Pandas
* Data preprocessing and analysis
* Pivot table generation
* Data visualization using Matplotlib
* Automated Excel report generation
* GUI development using Tkinter
* Practical implementation of business report automation

This project is intended for educational and learning purposes.
