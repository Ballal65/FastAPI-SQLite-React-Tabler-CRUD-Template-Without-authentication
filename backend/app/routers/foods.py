from fastapi import APIRouter
from .functions import get_nutrient_info

router = APIRouter(tags=['Food FDA'], prefix='/food')

@router.get('/{food_name}/{quantity_g}')
async def get_root(food_name:str = 'banana', quantity_g: float = 100.0):
    try:
        #print(f"Food Name: {food_name} \n Quantity:{quantity_g}")
        nutrient_info = await get_nutrient_info(food_name, quantity_g)
        return nutrient_info
    except Exception as e:
        return{"Error" : f"Erraor getting {food_name} data. {e}"}
