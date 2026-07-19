import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


import streamlit as st
import pandas as pd


from src.comparison import get_country_comparison

from src.charts import (
    create_country_comparison_chart,
    create_per_capita_comparison_chart
)

from src.ui import (
    dashboard_header,
    metric_card
)


st.set_page_config(
    page_title="Country Comparison",
    page_icon="🌎",
    layout="wide"
)


# ==========================================
# HEADER
# ==========================================

dashboard_header(
    "🌎 Global Country Comparison",
    "Compare GDP and GDP per capita among major world economies."
)


st.divider()


# ==========================================
# LOAD DATA
# ==========================================

comparison_data = get_country_comparison()

comparison_df = pd.DataFrame(comparison_data)



# ==========================================
# QUICK SNAPSHOT
# ==========================================

st.subheader("📌 Economic Comparison Snapshot")


highest_gdp = comparison_df.loc[
    comparison_df["GDP"].idxmax(),
    "Country"
]


highest_income = comparison_df.loc[
    comparison_df["GDP Per Capita"].idxmax(),
    "Country"
]


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        title="Countries Compared",
        value=str(len(comparison_df)),
        subtitle="Major economies analyzed",
        icon="🌎",
        color="#3B82F6"
    )


with col2:

    metric_card(
        title="Largest Economy",
        value=highest_gdp,
        subtitle="Highest GDP",
        icon="🏆",
        color="#22C55E"
    )


with col3:

    metric_card(
        title="Highest GDP Per Capita",
        value=highest_income,
        subtitle="Income indicator leader",
        icon="💰",
        color="#FACC15"
    )


st.divider()


# ==========================================
# TABLE
# ==========================================

st.subheader("📋 Comparison Table")


st.dataframe(
    comparison_df,
    use_container_width=True
)


st.divider()


# ==========================================
# GDP CHART
# ==========================================

st.subheader("📊 GDP Comparison")


gdp_chart = create_country_comparison_chart(
    comparison_df
)


st.plotly_chart(
    gdp_chart,
    use_container_width=True
)



# ==========================================
# GDP PER CAPITA CHART
# ==========================================

st.subheader("💰 GDP Per Capita Comparison")


income_chart = create_per_capita_comparison_chart(
    comparison_df
)


st.plotly_chart(
    income_chart,
    use_container_width=True
)



st.divider()


# ==========================================
# INSIGHT
# ==========================================

st.subheader("🤖 Economic Insight")


st.info(
    f"""
🌎 **Comparison Summary**

• {highest_gdp} currently leads in total GDP.

• {highest_income} has the highest GDP per capita
among the compared countries.

GDP measures economic size, while GDP per capita
shows average economic output per person.
"""
)