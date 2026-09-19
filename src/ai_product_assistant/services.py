from typing import TypedDict
from .models import *

# typedic ju ergänzen

def get_product_by_id(product_id: int, products: list[Product]) -> Product | None:
    
    for product in products:
        if product.id == product_id:
            return product

    return None 


def list_products(products: list[Product]) -> list[str]:
    result = []
    for product in products:
        result.append(product.name)

    return result
        
    
def search_product(product_name: str, products: list[Product]) -> Product | None:
    
    for product in products:
        if product.name.lower() == product_name.lower():
            return product
    return None


def add_product(product_id: int, name: str, price: int, stock: int, products: list[Product]) -> Product | None:

    new_product: Product = Product (
        id = product_id,
        name= name,
        price = price,
        stock = stock
    )

    existing_product = get_product_by_id(product_id, products)


    if existing_product is not None:
        return None

    products.append(new_product)

    return new_product

def update_stock(product_id: int, update_stock: int, products: list[Product]) -> Product | None:
    for product in products:
        if product.id == product_id:
            product.stock = update_stock
            return product  
    return None


def get_low_stocks(products: list[Product]) -> list[Product] | None:
    low_stock_products = []
    for product in products:
        if product.stock <= 2:
            low_stock_products.append(product)
    return low_stock_products




def delete_product(product_id: int, products: list[Product]) -> str | None :
    for product in products:
          if product.id == product_id:
                products.remove(product)
                return f"product deleted"
    return None