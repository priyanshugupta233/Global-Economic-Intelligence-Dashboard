import streamlit as st
import pandas as pd

from src.api import fetch_indicator
from src.countries import COUNTRIES

@st.cache_data(ttl=3600)
def get_top_gdp_countries():

    results = []


    for country_name, country_code in COUNTRIES.items():

        try:

            data = fetch_indicator(
                country_code,
                "NY.GDP.MKTP.CD"
            )


            latest = data[0]


            results.append(
                {
                    "Country": country_name,
                    "GDP": latest["value"],
                    "Year": latest["date"]
                }
            )


        except Exception:

            continue


    df = pd.DataFrame(results)


    df = df.dropna()


    df = df.sort_values(
        by="GDP",
        ascending=False
    )


    return df.head(10)