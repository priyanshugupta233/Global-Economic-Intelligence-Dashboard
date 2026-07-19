import streamlit as st

from src.api import fetch_indicator


@st.cache_data(ttl=3600)
def get_india_profile():

    india_code = "IND"


    # GDP
    gdp_data = fetch_indicator(
        india_code,
        "NY.GDP.MKTP.CD"
    )


    latest_gdp = None
    latest_year = None


    for item in gdp_data:
        if item["value"] is not None:
            latest_gdp = item["value"]
            latest_year = item["date"]
            break



    # GDP Per Capita

    income_data = fetch_indicator(
        india_code,
        "NY.GDP.PCAP.CD"
    )


    latest_income = None


    for item in income_data:
        if item["value"] is not None:
            latest_income = item["value"]
            break



    return {

        "Country": "India",

        "GDP": latest_gdp,

        "GDP Year": latest_year,

        "GDP Per Capita": latest_income

    }