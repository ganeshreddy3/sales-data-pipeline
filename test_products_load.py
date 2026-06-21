from src.extract_api import (
    extract_products_api
)

from src.transform_api import (
    transform_products
)

from src.load_products import (
    load_products
)


df = extract_products_api()

clean_df = transform_products(df)

load_products(clean_df)
