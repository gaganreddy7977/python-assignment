import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#--------- importing load_data,preprocessing data
from utils.dataset import load_data
from preprocessing import Global_filters

# ----------------- Page Config -----------------
st.set_page_config(page_title="Portfolio Risk Dashboard", page_icon="📊", layout="wide")

#--------------------importing pages-----------
# from pages.p1_Overview import render_page1
# from   segmentation import render_page2
# from  _demographics import render_page3
# from  _financials import render_page4
# from  _correlations import render_page5


# ----------------- Dashboard Header -----------------
st.title("🏠 Portfolio Risk Dashboard — Home")

#---------------page Navigation- Top of sidebar
page=st.sidebar.radio(
     "Navigate to:",
        (
            "1_Overview_&_Data_Quality",
            "Target & Risk Segmentation",
            "Demographics & Household Profile",
            "Financial Health & Affordability",
            "Correlations & Drivers "
        )
    )
    


# ----------------- Introduction -----------------
st.markdown("""
## 📖 Introduction  
The **Portfolio Risk Dashboard** helps you explore and monitor loan applications, borrower characteristics, and repayment outcomes.  
It is designed to give you a **360° view of portfolio health**, highlight potential risks, and support **data-driven decision-making**.
""")

# ----------------- How to Use -----------------
st.markdown("""
## 🛠 How to Use  
1. Use the **sidebar filters** (e.g., gender, education, housing, income) to customize the dataset view.  
2. Navigate through the **pages** to explore specific areas:  
   - **Overview & Data Quality** → Understand dataset coverage and quality.  
   - **Demographics & Household** → Analyze borrower profiles (age, gender, family).  
   - **Credit & Loan Behavior** → Explore loan amounts, income, and credit history.  
   - **Risk Segmentation** → Compare defaulters vs. non-defaulters across key features.  
3. Review **KPIs, charts, and insights** to identify trends and risk drivers.  
""")

# ----------------- Main Goal -----------------
st.markdown("""
## 🎯 Main Goal  
The main objective is to **assess portfolio risk** by analyzing borrower data and repayment behavior.  
This dashboard enables you to:  
- Detect **default patterns**.  
- Identify **high-risk borrower groups**.  
- Evaluate **data quality issues**.  
- Support **credit policy and decision-making**.  
""")

# ----------------- What You Will Learn -----------------
st.markdown("""
## 💡 What Will You Know by Using This?  
By interacting with the dashboard, you will discover:  
- 📊 **Overall Portfolio Health** → How many borrowers, what % default.  
- 👨‍👩‍👧 **Borrower Characteristics** → Who is more likely to default (by age, gender, education).  
- 💳 **Credit & Loan Behavior** → Which loan sizes or incomes are riskier.  
- ⚠️ **Key Risk Indicators** → Early warning signs from the dataset.  
""")




# ----------------- Page Links -----------------
st.markdown("""
---
### 🗂 Available Pages
- 📊 **Overview & Data Quality**  
- 👨‍👩‍👧 **Demographics & Household**  
- 💳 **Credit & Loan Behavior**  
- 📈 **Risk Segmentation**  
- 🛠 **Filters & Settings**  
""")
