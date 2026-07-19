from api import fetch_indicator


india_gdp = fetch_indicator(
    "IND",
    "NY.GDP.MKTP.CD"
)


print(india_gdp[:3])