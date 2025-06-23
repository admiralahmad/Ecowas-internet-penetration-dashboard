# 🌐 ECOWAS Internet Penetration Dashboard

A dynamic Streamlit-based dashboard that visualizes internet access, mobile subscriptions, and data affordability across West African countries (ECOWAS region).
<!-- Replace or remove if you don't have a screenshot yet -->

## 📊 Features

- 📈 Full-width line chart showing internet users over time
- 💰 Bar chart of average cost per GB of data
- 📶 Mobile subscriptions per 100 people
- 🌡️ Heatmap of internet penetration across countries and years
- 🗺️ Choropleth map of internet users by country
- 📥 Download filtered datasets
- 🎨 Clean UI with country/year filters

## 📁 Project Structure

ecowas-internet-dashboard/
├── dashboard.py # Main Streamlit app
├── data/
│ └── cleaned_internet_stats_ecowas.csv
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore

## 🛠️ Installation

```bash
git clone https://github.com/your-username/ecowas-internet-dashboard.git
cd ecowas-internet-dashboard
pip install -r requirements.txt

```

## 🛠️ Run
streamlit run dashboard.py
