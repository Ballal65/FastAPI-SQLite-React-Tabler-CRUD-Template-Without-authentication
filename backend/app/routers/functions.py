import os
import requests
from dotenv import load_dotenv

env_path = './.env'

if os.path.exists(env_path):
    print(f".env file found at {os.path.abspath(env_path)}")
    load_dotenv(env_path)
else:
    print(f".env file not found at {os.path.abspath(env_path)}")

api_key = os.getenv("API_KEY")


async def get_nutrient_info(food_name, quantity_g):
    global api_key
    
    # Endpoint for searching food items
    search_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    
    # Parameters for the request
    params = {
        "query": food_name,
        "api_key": api_key
    }
    
    # Make the search request
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        results = response.json()
        if results['totalHits'] > 0:
            # Assuming the first result is the most relevant one
            food_id = results['foods'][0]['fdcId']

            # Endpoint for fetching food details using its ID
            details_url = f"https://api.nal.usda.gov/fdc/v1/food/{food_id}"

            details_params = {"api_key": api_key}
            
            # Make the request for food details
            details_response = requests.get(details_url, params=details_params)
            if details_response.status_code == 200:
                details = details_response.json()

                nutrient_info = {
                    'Calories': 0,
                    'Protein': 0,
                    'Fat': 0,
                    'Carbohydrates': 0,
                    'Fiber': 0,
                    'Sugars': 0,
                    'Vitamins and Minerals': {}
                }
                
                # Loop through nutrients and extract information
                for nutrient in details.get('foodNutrients', []):
                    nutrient_name = nutrient.get('nutrient', {}).get('name')
                    amount = nutrient.get('amount')
                    if nutrient_name:
                        if 'Energy' in nutrient_name:
                            nutrient_info['Calories'] = amount
                        elif 'Protein' in nutrient_name:
                            nutrient_info['Protein'] = amount
                        elif 'Total lipid (fat)' in nutrient_name:
                            nutrient_info['Fat'] = amount
                        elif 'Carbohydrate, by difference' in nutrient_name:
                            nutrient_info['Carbohydrates'] = amount
                        elif 'Fiber' in nutrient_name:
                            nutrient_info['Fiber'] = amount
                        elif 'Sugars' in nutrient_name:
                            nutrient_info['Sugars'] = amount
                        else:
                            # Assuming all other nutrients are vitamins/minerals
                            nutrient_info['Vitamins and Minerals'][nutrient_name] = amount
                
                # Adjust amounts based on the quantity specified by the user
                for key in ['Calories', 'Protein', 'Fat', 'Carbohydrates', 'Fiber', 'Sugars']:
                    nutrient_info[key] = (nutrient_info[key] * quantity_g) / 100
                
                for mineral in nutrient_info['Vitamins and Minerals']:
                    nutrient_info['Vitamins and Minerals'][mineral] = (nutrient_info['Vitamins and Minerals'][mineral] * quantity_g) / 100
                
                return nutrient_info