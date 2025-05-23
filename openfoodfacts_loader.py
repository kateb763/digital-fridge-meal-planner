import requests
import pandas as pd

def fetch_openfoodfacts_data(page_size=1000):
    """
    Fetches product data from the Open Food Facts API and returns it as a pandas DataFrame.

    Parameters:
    - page_size (int): Number of products to fetch per API request (default is 1000).

    Returns:
    - pandas.DataFrame: A DataFrame containing selected product information, including:
        - product_name
        - brands
        - ingredients_text
        - nutriments.energy-kcal_100g
        - nutriments.proteins_100g
        - nutriments.carbohydrates_100g
        - nutriments.fat_100g

    Notes:
    - The function filters the data to include only relevant columns.
    - Rows with missing 'product_name' values are dropped.
    - Data is normalized from nested JSON format for easier analysis.
    """
    url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        'search_simple': 1,
        'action': 'process',
        'json': 1,
        'page_size': page_size
    }
    response = requests.get(url, params=params)
    products = response.json().get('products', [])
    df = pd.json_normalize(products)
    
    # Keep only relevant columns
    relevant_cols = [
        'product_name', 'brands', 'ingredients_text',
        'nutriments.energy-kcal_100g', 'nutriments.proteins_100g',
        'nutriments.carbohydrates_100g', 'nutriments.fat_100g'
    ]
    df = df[[col for col in relevant_cols if col in df.columns]]
    df.dropna(subset=['product_name'], inplace=True)
    print(df)
    return df


