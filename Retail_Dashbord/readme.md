🛍️ Superstore Sales Analysis Dashboard

An interactive Streamlit dashboard for analyzing sales, profit, and regional performance of a Superstore dataset.
The app allows you to either upload your own dataset or use the provided default dataset.

🚀 Features

📊 Overview Dashboard – Key metrics and insights

🛒 Sales Analysis – Trends and performance by product & time

💰 Profit Analysis – Identify profitability drivers

🌍 Region Analysis – Regional contribution to sales & profits

📦 Category Analysis – Category- and subcategory-level breakdowns

📂 Upload Support – Upload your own .csv or .xls/.xlsx files

📂 Project Structure
├── Home.py                 # Main Streamlit app entry point
├── utils/
│   └── load_data.py        # Data loading and preprocessing functions
├── Source Sales Data.xls   # Default sample dataset
├── requirments.txt         # Python dependencies
└── README.md               # Project documentation

🛠️ Installation

Clone the repository

git clone https://github.com/your-username/superstore-dashboard.git
cd superstore-dashboard


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirments.txt

▶️ Usage

Run the Streamlit app:

streamlit run Home.py


Then open the app in your browser at:

http://localhost:8501

📊 Data

The default dataset is Source Sales Data.xls, which contains sales, profit, and customer information for a sample superstore.

You can also upload your own dataset via the dashboard (supported formats: .csv, .xls, .xlsx).

📦 Requirements

The main dependencies are:

streamlit

pandas

numpy

matplotlib

altair

scikit-learn

openpyxl

(Full list available in requirments.txt)