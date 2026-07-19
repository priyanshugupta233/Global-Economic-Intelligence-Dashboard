from src.comparison import get_country_comparison


data = get_country_comparison()


for item in data:
    print(item)