import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


import streamlit as st


from src.world_map import get_world_gdp_data
from src.charts import create_world_gdp_map

from src.ui import (
    dashboard_header,
    metric_card
)


st.set_page_config(
    page_title="World GDP Map",
    page_icon="🌍",
    layout="wide"
)


# ==================================
# HEADER
# ==================================

dashboard_header(
    "🌍 Global Economic Intelligence Map",
    "Explore GDP distribution across countries using interactive world visualization."
)


st.divider()


# ==================================
# DATA
# ==================================

df = get_world_gdp_data()



# ==================================
# KPI SECTION
# ==================================

st.subheader("📌 Global GDP Map Snapshot")


highest_country = df.loc[
    df["GDP"].idxmax(),
    "Country"
]


highest_gdp = df.loc[
    df["GDP"].idxmax(),
    "GDP"
]


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        title="Countries Mapped",
        value=str(len(df)),
        subtitle="Global economic coverage",
        icon="🌎",
        color="#3B82F6"
    )


with col2:

    metric_card(
        title="Largest Economy",
        value=highest_country,
        subtitle="Highest GDP",
        icon="🏆",
        color="#22C55E"
    )


with col3:

    metric_card(
        title="Maximum GDP",
        value=f"${highest_gdp/1e12:.2f}T",
        subtitle="Economic size",
        icon="💰",
        color="#FACC15"
    )


st.divider()


# ==================================
# MAP
# ==================================

st.subheader("🗺️ Interactive World GDP Visualization")


fig = create_world_gdp_map(df)


st.plotly_chart(
    fig,
    use_container_width=True
)



st.divider()


# ==================================
# TABLE
# ==================================

st.subheader("📋 World GDP Data")


st.dataframe(
    df,
    use_container_width=True
)



st.divider()


# ==================================
# INSIGHT
# ==================================

st.subheader("🤖 Global Economic Insight")


st.info(
    f"""
🌍 **World Economy Observation**

{highest_country} currently represents the largest
GDP value in this dataset.

The world economy is distributed across multiple
regions, with major contributions from North America,
Europe, and Asia.
"""
)


st.success(
    "🗺️ World Map Intelligence Module Completed"
)