import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from src.ui import (
    setup_page,
    dashboard_header,
    metric_card,
    create_sidebar
)

# -----------------------------
# Page Configuration
# -----------------------------
setup_page(
    "Global Economic Intelligence Dashboard",
    "🌍"
)

create_sidebar()

# -----------------------------
# Header
# -----------------------------
dashboard_header(
    "🌍 Global Economic Intelligence Dashboard",
    "An interactive platform for exploring global economic trends using live World Bank data."
)

st.divider()

# -----------------------------
# About Section
# -----------------------------
st.subheader("📌 About This Dashboard")

st.info(
    """
### 🌍 Global Economic Intelligence Dashboard

Explore and compare live economic data from the **World Bank Open Data API**.

This dashboard provides interactive visualizations,
country comparisons, GDP trends, and economic insights
through an intuitive interface.
"""
)

st.divider()

# -----------------------------
# Dashboard Overview
# -----------------------------
st.subheader("📊 Dashboard Overview")

col1, col2 = st.columns(2)

with col1:
    metric_card(
        title="Countries Supported",
        value="190+",
        subtitle="Countries with economic data",
        icon="🌍",
        color="#3B82F6"
    )

with col2:
    metric_card(
        title="Economic Indicators",
        value="GDP",
        subtitle="Live World Bank indicators",
        icon="📈",
        color="#A855F7"
    )

col3, col4 = st.columns(2)

with col3:
    metric_card(
        title="Dashboard Pages",
        value="6",
        subtitle="Interactive analysis pages",
        icon="🗺️",
        color="#FACC15"
    )

with col4:
    metric_card(
        title="Built With",
        value="Python",
        subtitle="Streamlit • Plotly • Pandas",
        icon="⚡",
        color="#FB923C"
    )

st.divider()

# -----------------------------
# Modules
# -----------------------------
st.subheader("🚀 Available Modules")

st.markdown(
    """
### 🌍 Global Overview
- GDP rankings
- Historical GDP trends

### 🇮🇳 India Analysis
- GDP
- GDP Per Capita
- Economic overview

### 🌎 Country Comparison
- Compare multiple countries
- Interactive comparison charts

### 🤖 Economic Insights
- Automated economic observations

### 🗺️ World Map
- Interactive GDP visualization
"""
)

st.success(
    "✅ Dashboard Version 3.0 - Professional UI Upgrade Started"
)

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.caption("📡 Data Source: World Bank Open Data API")
st.caption("👨‍💻 Built with Python • Pandas • Plotly • Streamlit")
st.caption("© 2026 Global Economic Intelligence Dashboard")