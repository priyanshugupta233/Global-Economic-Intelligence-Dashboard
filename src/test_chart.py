from api import fetch_indicator
from data_engine import clean_indicator_data
from charts import create_gdp_line_chart


raw_data = fetch_indicator(
    "IND",
    "NY.GDP.MKTP.CD"
)


india_df = clean_indicator_data(
    raw_data,
    "India"
)


chart = create_gdp_line_chart(
    india_df
)


chart.show()