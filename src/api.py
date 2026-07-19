import requests
import streamlit as st


@st.cache_data(ttl=3600)
def fetch_indicator(country_code, indicator):

    url = (
        f"https://api.worldbank.org/v2/country/"
        f"{country_code}/indicator/{indicator}"
    )

    params = {
        "format": "json",
        "per_page": 100
    }


    response = requests.get(
        url,
        params=params
    )


    data = response.json()


    if len(data) < 2:
        return []


    return data[1]