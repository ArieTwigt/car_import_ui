import requests
from utils import ENDPOINT
from typing import List, Dict


def import_cars_by_brand(brand: str) -> List[Dict]:
    '''
    
    Import cars from RDW
    
    '''

    # uppercase the brand
    brand_upper = brand.upper().strip()

    # append the brand to the endpoint
    endpoint_brand = f"{ENDPOINT}?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint_brand)

    # get the data
    data = response.json()
    
    return data