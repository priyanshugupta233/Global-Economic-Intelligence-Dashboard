import streamlit as st
import pandas as pd

from src.api import fetch_indicator


@st.cache_data(ttl=3600)
def get_world_gdp_data():

    countries = {
        "United States": "USA",
        "China": "CHN",
        "India": "IND",
        "Japan": "JPN",
        "Germany": "DEU",
        "United Kingdom": "GBR",
        "France": "FRA",
        "Italy": "ITA",
        "Canada": "CAN",
        "Russia": "RUS"
    }

    results = []

    for country, code in countries.items():

        data = fetch_indicator(
            code,
            "NY.GDP.MKTP.CD"
        )

        latest_gdp = None

        for item in data:
            if item["value"] is not None:
                latest_gdp = item["value"]
                break

        results.append({
            "Country": country,
            "ISO": code,
            "GDP": latest_gdp
        })

    return pd.DataFrame(results)