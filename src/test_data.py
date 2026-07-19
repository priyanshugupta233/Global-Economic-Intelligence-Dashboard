from api import fetch_indicator
from data_engine import clean_indicator_data


raw_data = fetch_indicator(
    "IND",
    "NY.GDP.MKTP.CD"
)


india_df = clean_indicator_data(
    raw_data,
    "India"
)


print(india_df.head())