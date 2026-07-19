import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


import streamlit as st
import pandas as pd


from src.ranking import get_top_gdp_countries
from src.api import fetch_indicator

from src.charts import (
    create_gdp_ranking_chart,
    create_gdp_line_chart
)

from src.ui import (
    dashboard_header,
    metric_card
)


st.set_page_config(
    page_title="Global Overview",
    page_icon="🌍",
    layout="wide"
)


# ===============================
# Header
# ===============================

dashboard_header(
    "🌍 Global Economic Overview",
    "Explore global GDP rankings and historical economic trends using World Bank data."
)


st.divider()


# ===============================
# Data
# ===============================

top10 = get_top_gdp_countries()


# ===============================
# KPI Snapshot
# ===============================

st.subheader("📌 Global Economic Snapshot")


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        title="Countries Analyzed",
        value=str(len(top10)),
        subtitle="Top GDP economies",
        icon="🌎",
        color="#3B82F6"
    )


with col2:

    metric_card(
        title="Largest Economy",
        value=top10.iloc[0]["Country"],
        subtitle="Highest GDP globally",
        icon="🏆",
        color="#22C55E"
    )


with col3:

    metric_card(
        title="Largest GDP",
        value=f"${top10.iloc[0]['GDP']/1e12:.2f}T",
        subtitle="Economic size",
        icon="💰",
        color="#FACC15"
    )


st.divider()


# ===============================
# GDP Ranking
# ===============================

st.subheader("🏆 Top 10 GDP Countries")


st.dataframe(
    top10,
    use_container_width=True
)


st.subheader("📊 GDP Ranking Visualization")


ranking_chart = create_gdp_ranking_chart(top10)


st.plotly_chart(
    ranking_chart,
    use_container_width=True
)



st.divider()


# ===============================
# GDP History
# ===============================

st.subheader("📈 GDP Growth History")


country = st.selectbox(
    "Select Country",
    [
        "India",
        "United States",
        "China",
        "Japan",
        "Germany"
    ]
)


country_codes = {

    "India": "IND",
    "United States": "USA",
    "China": "CHN",
    "Japan": "JPN",
    "Germany": "DEU"

}


raw = fetch_indicator(
    country_codes[country],
    "NY.GDP.MKTP.CD"
)


history = []


for item in raw:

    if item["value"] is not None:

        history.append(
            {
                "Year": int(item["date"]),
                "Value": item["value"],
                "Country": country
            }
        )


history_df = pd.DataFrame(history)


history_df = history_df.sort_values("Year")


line_chart = create_gdp_line_chart(history_df)


st.plotly_chart(
    line_chart,
    use_container_width=True
)