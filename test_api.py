from src.extract_api import extract_products_api
from src.transform_api import transform_products

df = extract_products_api()

clean_df = transform_products(df)

print(clean_df.head())
