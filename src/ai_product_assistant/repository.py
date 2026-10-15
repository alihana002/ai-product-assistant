import json    

from .models import *
from dataclasses import asdict
import requests


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
        try:
            obj_product =  Product(**product_dic)
        except TypeError:
            print("Missing value")
            
        new_list.append(obj_product)
        
    return new_list



def get_api_product(product_id: int) -> Product | None:
    try:
        r_p = requests.get(f'https://dummyjson.com/products/{product_id}')
        r_p.raise_for_status()
        r_p_json = r_p.json()
    except requests.HTTPError:
        
        if r_p.status_code == 404 :
            return None 
        raise
        
  

            
    new_product : Product = Product (
        id =  r_p_json["id"],
        name = r_p_json["title"],
        price = r_p_json["price"], 
        stock = r_p_json["stock"]

    )

    
    return new_product
     
 

