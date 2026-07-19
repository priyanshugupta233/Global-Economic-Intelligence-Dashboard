import pandas as pd


def clean_indicator_data(data, country_name):
    """
    Convert World Bank API response into clean dataframe.
    """

    records = []

    for item in data:

        records.append(
            {
                "Country": country_name,
                "Year": int(item["date"]),
                "Value": item["value"]
            }
        )

    df = pd.DataFrame(records)

    df = df.dropna()

    df = df.sort_values(
        "Year"
    )

    return df
