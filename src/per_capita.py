import pandas as pd
from src.api import fetch_indicator

import streamlit as st
def get_gdp_per_capita():

    countries = {
        "United States": "USA",
        "China": "CHN",
        "Germany": "DEU",
        "Japan": "JPN",
        "India": "IND",
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
            "NY.GDP.PCAP.CD"
        )

        latest = data[0]


        results.append(
            {
                "Country": country,
                "GDP Per Capita": latest["value"],
                "Year": latest["date"]
            }
        )


    df = pd.DataFrame(results)


    df = df.sort_values(
        by="GDP Per Capita",
        ascending=False
    )


    return df