import json    

from .models import *
from dataclasses import asdict


def save_products(products:list[Product]) -> None:
    new_list = []
    for product in products:
        obj_to_dic: dict = asdict(product)
        new_list.append(obj_to_dic)
    with open("data/products.json", "w", encoding="utf-8") as f:
            json.dump(new_list, f, indent=4)
  
        



def load_products()->list[Product] | None:
    try:
        with open('data/products.json', 'r', encoding="utf-8") as f:
            products = json.load(f)
    except FileNotFoundError:
        print("File not found")
        return None 

    except json.JSONDecodeError:
        print("Ivalid syntax in data")
        return None 
    new_list = []
    for product_dic in products:
        obj_product =  Product(**product_dic)
        new_list.append(obj_product)
        
    return new_list




