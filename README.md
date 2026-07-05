# 🚨 Customer Churn Prediction Dashboard

[![View Notebook](https://img.shields.io/badge/Jupyter-View_Notebook-orange?logo=Jupyter)](https://nbviewer.org/github/himangana/customer_churn_dashboard/blob/main/Churn_Project.ipynb)

This is my first data science and web application project! It analyzes customer data, identifies customers who are at high risk of leaving (churning), and displays them on an interactive dashboard.

## 📊 Project Overview
The project is split into two parts:
1. **Jupyter Notebook (`Churn_Project.ipynb`)**: Performs the initial data analysis on the customer dataset, processes the churn risk, and outputs the results to `churn_risk_data.csv`.
2. **Streamlit App (`app.py`)**: Reads the processed data and displays an executive dashboard showing:
   * Key Performance Indicators (KPIs) like the number of critical-risk customers and average risk.
   * An interactive, sortable action list of the highest-risk customers.
   * Interactive charts visualizing the relationship between customer risk and tenure.

---

## 🛠️ Tech Stack
* **Python**
* **Pandas** (for data manipulation)
* **Streamlit** (for the web application dashboard)
* **Jupyter Notebook** (for prototyping and data analysis)

---

## 🚀 How to Run the Project Locally

### 1. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install pandas streamlit ipykernel
```

### 2. Generate the Scored Data
Open and run all cells in the Jupyter notebook `Churn_Project.ipynb`. This will create the dataset file: `churn_risk_data.csv`.

### 3. Start the Dashboard
In your terminal, navigate to this project directory and start the Streamlit web server:
```bash
python -m streamlit run app.py
```
This will automatically open the dashboard in your default web browser (usually at `http://localhost:8501`).

---

## 💡 What I Learned from this Project
* How to load and manipulate datasets using **Pandas**.
* How to structure Jupyter notebooks for data analysis.
* Building interactive web apps in Python with **Streamlit**.
* Optimizing data visualizations (sampling, aggregation, and caching) for faster browser performance.
