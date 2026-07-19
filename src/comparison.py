import streamlit as st

from src.api import fetch_indicator


@st.cache_data(ttl=3600)
def get_country_comparison():

    countries = {
        "India": "IND",
        "China": "CHN",
        "United States": "USA"
    }


    results = []


    for country, code in countries.items():


        # GDP
        gdp_data = fetch_indicator(
            code,
            "NY.GDP.MKTP.CD"
        )


        gdp = None


        for item in gdp_data:
            if item["value"] is not None:
                gdp = item["value"]
                break



        # GDP Per Capita

        income_data = fetch_indicator(
            code,
            "NY.GDP.PCAP.CD"
        )


        income = None


        for item in income_data:
            if item["value"] is not None:
                income = item["value"]
                break



        results.append(
            {
                "Country": country,
                "GDP": gdp,
                "GDP Per Capita": income
            }
        )


    return results