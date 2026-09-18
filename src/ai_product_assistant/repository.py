import json     
from .models import *


def save_products(products:list[Product]) -> None:
    with open("data/products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4)
   



def load_products()->list[Product]:
    with open('data/products.json', 'r', encoding="utf-8") as f:
        json_products = json.load(f)
        return json_products