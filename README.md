# 🤖 AI Business Intelligence Reporting Agent

## 📌 Project Overview

The AI Business Intelligence Reporting Agent is an automated analytics solution that combines data processing, KPI generation, AI-powered reporting, and dashboard visualization.

The project uses **n8n** for workflow automation, **Google Gemini AI** for business insight generation, and **Streamlit** for interactive dashboard visualization.

The system is designed to ingest raw sales data, identify data quality issues, clean and standardize records, calculate business KPIs, and present actionable insights through a dashboard.

---

## 🎯 Objectives

* 📥 Automate sales data ingestion and processing
* 🔍 Detect and report data quality issues
* 🧹 Clean and standardize inconsistent data
* 📊 Generate key business performance metrics
* 🤖 Produce AI-generated business insights using Gemini AI
* 📈 Visualize results through an interactive dashboard

---

## 🛠️ Technology Stack

### ⚙️ Workflow Automation

* n8n

### 🤖 Artificial Intelligence

* Google Gemini AI

### 📊 Dashboard Development

* Streamlit
* Plotly

### 🐍 Data Processing

* Python
* Pandas

### 📂 Data Source

* Excel / CSV Files

---

## 🏗️ Current Workflow Architecture

```text
Raw Sales Data (Excel)
          │
          ▼
Read File (n8n)
          │
          ▼
Extract Data
          │
          ├───────────────┐
          ▼               ▼
Data Cleaning      Quality Check
          │               │
          ▼               ▼
KPI Calculation   Issue Aggregation
          │               │
          └───────┬───────┘
                  ▼
             Gemini AI
                  ▼
         Business Insights
                  ▼
      Streamlit Dashboard
```
<img width="1364" height="677" alt="image" src="https://github.com/user-attachments/assets/2330b7fd-6b58-4696-b0fe-fa22096b71d8" />


---

## 🔍 Data Quality Checks Implemented

The workflow currently detects:

* ❌ Missing Customer Names
* ❌ Invalid Quantities
* ❌ Negative Quantities
* ❌ Missing Unit Prices
* ❌ Invalid Category Values
* ❌ Inconsistent State Names
* ❌ Extra Whitespace in Text Fields

---

## 🧹 Data Cleaning Operations

### 👤 Customer Data Cleaning

* Trims unnecessary spaces
* Replaces missing customer names with placeholder values

### 📦 Product Standardization

* Standardizes product naming
* Removes inconsistent capitalization

### 📍 State Standardization

Converts:

* WB
* west bengal
* Kolkata

into:

```text
West Bengal
```

### 🔢 Quantity Validation

* Detects invalid numeric values
* Flags negative quantities

### 💰 Price Validation

* Detects missing or invalid unit prices

---

## 📈 KPI Metrics Generated

### 📊 Business KPIs

* Total Orders
* Total Revenue
* Top Product
* Top Product Revenue
* Top Salesperson
* Top Salesperson Revenue

### Example Output

| KPI                     | Value    |
| ----------------------- | -------- |
| Total Orders            | 21       |
| Total Revenue           | ₹489,900 |
| Top Product             | Laptop   |
| Top Product Revenue     | ₹275,000 |
| Top Salesperson         | Amit     |
| Top Salesperson Revenue | ₹292,000 |

---

## 🤖 AI-Powered Business Analysis

Google Gemini AI is integrated into the workflow to generate:

* 📝 Executive Summary
* 💡 Business Insights
* 📊 KPI Interpretation
* 💰 Revenue Analysis
* 🎯 Strategic Recommendations
* ⚠️ Data Quality Observations

### Sample Insight

> Revenue reached ₹489,900 across 21 valid orders. Laptop was the highest-performing product category, while Amit generated the highest revenue among sales representatives.

---

## 📊 Streamlit Dashboard Features

### 📌 KPI Cards

* 💰 Total Revenue
* 📦 Total Orders
* 🏆 Top Product
* 👨‍💼 Top Salesperson

### 📈 Visualizations

* Revenue by Product
* Revenue by Salesperson
* Revenue by Category

### 📋 Data View

* Cleaned Sales Dataset Table

<img width="1320" height="602" alt="image" src="https://github.com/user-attachments/assets/4f737321-3b88-4a57-a807-ba03f8721eff" />

<img width="1328" height="509" alt="image" src="https://github.com/user-attachments/assets/634a8bd9-f194-4c6c-8a23-fc098e8eaf39" />

<img width="1284" height="493" alt="image" src="https://github.com/user-attachments/assets/a890178c-ae16-47c1-a9d2-d540fa541791" />

<img width="1280" height="480" alt="image" src="https://github.com/user-attachments/assets/eaf7dea0-12b9-484c-8327-af2325094c6d" />

---

## 📁 Project Structure

```text
AI_BI_Reporting_Agent/
│
├── app.py
├── requirements.txt
├── File.csv
├── workflow.json
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI_BI_Reporting_Agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run app.py
```

### Start n8n

```bash
n8n
```

---

## ✅ Current Project Status

### Completed

* ✅ Data ingestion using n8n
* ✅ Data quality validation
* ✅ Data cleaning workflow
* ✅ KPI generation
* ✅ Gemini AI integration
* ✅ Streamlit dashboard
* ✅ Revenue visualizations

### In Progress

* 🔄 Automated file monitoring
* 🔄 Direct dashboard refresh from n8n
* 🔄 AI insight integration into dashboard
* 🔄 Power BI dashboard version
* 🔄 End-to-end workflow automation

---

## 🔮 Future Enhancements

* 📥 Automated file upload detection
* ⚡ Real-time dashboard updates
* 📊 Power BI integration
* 📄 PDF report generation
* 📧 Email report distribution
* 📉 Historical trend analysis
* 🔮 Predictive analytics
* 🗄️ Database integration

---

## 👩‍💻 Author

**Debasmita Sen**

### Areas of Interest

* 📊 Business Intelligence
* 📈 Data Analytics
* ⚙️ Workflow Automation
* 🤖 Artificial Intelligence
* 🎨 Dashboard Development
