import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


import streamlit as st
import pandas as pd


from src.comparison import get_country_comparison

from src.ui import (
    dashboard_header,
    metric_card
)


st.set_page_config(
    page_title="Economic Insights",
    page_icon="🤖",
    layout="wide"
)


# ==========================
# HEADER
# ==========================

dashboard_header(
    "🤖 Economic Intelligence Insights",
    "Automated observations generated from global economic indicators."
)


st.divider()


# ==========================
# DATA
# ==========================

comparison_df = pd.DataFrame(
    get_country_comparison()
)


largest_gdp = comparison_df.loc[
    comparison_df["GDP"].idxmax()
]


highest_income = comparison_df.loc[
    comparison_df["GDP Per Capita"].idxmax()
]


india = comparison_df[
    comparison_df["Country"] == "India"
].iloc[0]



# ==========================
# INSIGHT SNAPSHOT
# ==========================

st.subheader("📌 Economic Intelligence Snapshot")


col1, col2, col3 = st.columns(3)


with col1:

    metric_card(
        title="Largest Economy",
        value=largest_gdp["Country"],
        subtitle=f"${largest_gdp['GDP']/1e12:.2f} Trillion GDP",
        icon="🏆",
        color="#22C55E"
    )


with col2:

    metric_card(
        title="Highest GDP Per Capita",
        value=highest_income["Country"],
        subtitle=f"${highest_income['GDP Per Capita']:,.0f} per person",
        icon="💰",
        color="#FACC15"
    )


with col3:

    metric_card(
        title="India GDP",
        value=f"${india['GDP']/1e12:.2f}T",
        subtitle=f"Per Capita ${india['GDP Per Capita']:,.0f}",
        icon="🇮🇳",
        color="#F97316"
    )


st.divider()


# ==========================
# DETAILED INSIGHTS
# ==========================

st.subheader("🧠 Generated Economic Observations")


st.success(
    f"""
🏆 **Largest Economy**

{largest_gdp['Country']} currently leads the selected countries
with a GDP of ${largest_gdp['GDP']/1e12:.2f} Trillion.
"""
)


st.info(
    f"""
💰 **Highest GDP Per Capita**

{highest_income['Country']} has the highest GDP per capita
at approximately ${highest_income['GDP Per Capita']:,.0f}.
"""
)


st.warning(
    f"""
🇮🇳 **India Analysis**

India has a GDP of ${india['GDP']/1e12:.2f} Trillion,
while GDP per capita is ${india['GDP Per Capita']:,.0f}.

This shows the difference between total economic size
and average economic output per person.
"""
)



st.divider()


# ==========================
# SUMMARY
# ==========================

st.subheader("📋 Key Takeaways")


st.markdown(
"""
- 🌍 GDP represents the total size of an economy.
- 💰 GDP per capita helps understand average economic output per person.
- 🇺🇸 Large economies often have high GDP because of their market size.
- 🇮🇳 India shows strong economic scale with a growing global position.
- 📊 Economic indicators should be analyzed together for better understanding.
"""
)


st.success(
    "🤖 Economic Intelligence Module Completed"
)