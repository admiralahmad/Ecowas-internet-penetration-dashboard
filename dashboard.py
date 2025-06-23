
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="ECOWAS Internet Penetration Dashboard",
    layout="wide",
    page_icon="🌍"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_internet_stats_ecowas.csv")
    return df

df = load_data()

# Sidebar
with st.sidebar:
    st.title("🌐 ECOWAS Internet Explorer")
    selected_countries = st.multiselect("Select Countries", df["Country"].unique(), default=df["Country"].unique())
    selected_years = st.multiselect("Select Years", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
    st.markdown("---")
    st.markdown("Developed by Ahmad Saidu")

# Filter data
filtered_df = df[(df["Country"].isin(selected_countries)) & (df["Year"].isin(selected_years))]

# Title and overview
st.title("📊 West Africa Internet Penetration Dashboard")
st.markdown("Track internet access, mobile connectivity, and data affordability across ECOWAS countries.")

# Layout for charts
st.subheader("📈 Internet Users (% of population) Over Time")
fig, ax = plt.subplots(figsize=(12, 6))
for country in selected_countries:
    country_data = filtered_df[filtered_df["Country"] == country]
    ax.plot(country_data["Year"], country_data["Internet_Users_Percentage"], marker='o', label=country)
ax.set_ylabel("Internet Users (%)")
ax.set_xlabel("Year")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Country")
ax.set_title("Internet Users Over Time in ECOWAS Countries")
ax.grid(True)   
st.pyplot(fig)


st.subheader("💰 Average Cost per GB (USD)")
cost_data = filtered_df.groupby("Country")["Cost_Per_GB_USD"].mean().sort_values()
st.bar_chart(cost_data)

# Full-width chart
st.subheader("📶 Mobile Subscriptions Per 100 People")
mobile_chart = filtered_df.groupby("Country")["Mobile_Subscriptions"].mean().sort_values()
st.bar_chart(mobile_chart)

# Heatmap
st.subheader("🌡️ Heatmap: Internet Users Over Time(in Millions)")
pivot = filtered_df.pivot_table(index="Country", columns="Year", values="Internet_Users_Percentage")
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Choropleth Map
st.subheader("🗺️ Internet Penetration Map (Latest Year Selected)")

# Use the most recent year in the filter
latest_year = max(selected_years)
latest_df = filtered_df[filtered_df["Year"] == latest_year]

# Mapping country names to ISO Alpha-3 codes for ECOWAS
country_code_map = {
    "Benin": "BEN", "Burkina Faso": "BFA", "Cape Verde": "CPV", "Côte d'Ivoire": "CIV",
    "Gambia": "GMB", "Ghana": "GHA", "Guinea": "GIN", "Guinea-Bissau": "GNB",
    "Liberia": "LBR", "Mali": "MLI", "Niger": "NER", "Nigeria": "NGA",
    "Senegal": "SEN", "Sierra Leone": "SLE", "Togo": "TGO"
}

latest_df["iso_alpha"] = latest_df["Country"].map(country_code_map)

fig = px.choropleth(
    latest_df,
    locations="iso_alpha",
    color="Internet_Users_Percentage",
    hover_name="Country",
    color_continuous_scale="YlGnBu",
    projection="natural earth",
    title=f"Internet Users in {latest_year} (% of Population)"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Download button
st.download_button("📥 Download Filtered Data", data=filtered_df.to_csv(index=False), file_name="filtered_data.csv")

# Footer
st.markdown("---")
st.markdown("📌 Built with ❤️ by Ahmad Saidu")
