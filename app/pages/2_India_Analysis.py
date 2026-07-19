import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


import streamlit as st
import pandas as pd


from src.india import get_india_profile
from src.per_capita import get_gdp_per_capita
from src.charts import create_per_capita_chart

from src.ui import (
    dashboard_header,
    metric_card
)


st.set_page_config(
    page_title="India Analysis",
    page_icon="🇮🇳",
    layout="wide"
)


# ==================================
# HEADER
# ==================================

dashboard_header(
    "🇮🇳 India Economic Intelligence",
    "Explore India's economic performance, GDP, and GDP per capita trends using World Bank data."
)


st.divider()


# ==================================
# INDIA PROFILE
# ==================================

india = get_india_profile()


st.subheader("📌 India Economic Snapshot")


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        title="Country",
        value=india["Country"],
        subtitle="Economic profile",
        icon="🇮🇳",
        color="#F97316"
    )


with col2:

    metric_card(
        title="GDP",
        value=f"${india['GDP']/1e12:.2f}T",
        subtitle="Total economic output",
        icon="💵",
        color="#22C55E"
    )


with col3:

    metric_card(
        title="GDP Per Capita",
        value=f"${india['GDP Per Capita']:,.0f}",
        subtitle="Average income indicator",
        icon="👤",
        color="#3B82F6"
    )


st.divider()


# ==================================
# GDP PER CAPITA
# ==================================

st.subheader("💰 GDP Per Capita Analysis")


per_capita_df = get_gdp_per_capita()


st.dataframe(
    per_capita_df,
    use_container_width=True
)


st.subheader("📊 GDP Per Capita Visualization")


chart = create_per_capita_chart(
    per_capita_df
)


st.plotly_chart(
    chart,
    use_container_width=True
)


st.divider()


# ==================================
# INSIGHT
# ==================================

st.subheader("🤖 Economic Insight")


st.info(
    """
🇮🇳 India is one of the world's largest economies.

GDP and GDP per capita analysis helps understand
the country's economic scale and individual prosperity.
"""
)
