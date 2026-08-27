def main() -> None:
    """
    while True:
        try:
            product_id = int(input("Welche id? "))
        except ValueError:
            print("Es wird eine Zahl erwartet")
            continue
        
        product = get_product(product_id)
        if product is None:
            print("Diese ID gibt es nicht")
        else:
            print(f"Name: {product["name"]}")
            print(f"Preis: {product["price"]}")
            break
    
    product_list = list_products(products)
    print(f"Die Produkte sind vorhanden: {product_list}")

    product_name = (input("Welches Produkt? "))
   
    found_product = search_product(product_name)
    if found_product is None:
        print("Dieser Produkt existiert nicht")

    else:
        print(f"Das folgende Produkt: {found_product["name"]}, {found_product["price"]}")

    
    
    name = input("Ein neues Produkt hinzufügen: ")
    while True:
        try:
            product_id = int(input("Eine Id: "))
        except ValueError:
            print("Es wird eine Zahl erwartet")
            continue
       

        existing_product = get_product(product_id)

        if existing_product is not None:
            print("die id existiert bereits")
            continue
        break    
    while True:
         try:
            price = int(input("Einen Preis: "))
         except ValueError:
            print("Es wird eine Zahl erwartet")
            continue

         new_product = add_product(product_id, name, price)
         print(new_product)
         break
   

    while True:
                try:
                    input_product_id = int(input("Enter a productid for updating stock: "))
                except ValueError:
                    print("You need to enter a number")
                    continue             

                product = get_product(input_product_id)

                if product is None:
                    print("id does not exist")
                    continue

                
                while True:
                        try:
                            input_stock = int(input("Enter a new Stock: "))
                        except ValueError:
                                print("Enter a number")
                                continue
                        break
                
                

                update_product = update_stock(input_product_id, input_stock)
                print(update_product)
               
                    
                break
    """
    low_stock_list = get_low_stocks(products)
    print(low_stock_list)
    


    

products = [
    {"id": 1, "name": "Tisch", "price": 299, "stock": 4},
    {"id": 2, "name": "Stuhl", "price": 99, "stock": 2},
    {"id": 3, "name": "Schrank", "price": 599, "stock": 2}
]



def get_product(product_id: int) -> list[dict[str, int | str]]:
    for product in products:
        if product["id"] == product_id:
            return product

    return None 


def list_products(products: list[dict[str, int | str]]) -> list[str]:
    result = []

    for product in products:
        result.append(product["name"])

    return result
        
    
def search_product(product_name):
    for product in products:
        if product["name"].lower() == product_name.lower():
            return product
    return None


def add_product(id: int, name: str, price: int):

    new_product = {
        "id": id,
        "name": name,
        "price": price 
    }

    products.append(new_product)

    return new_product

def update_stock(product_id: id, update_stock: id):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = update_stock
            return product  
    return None


def get_low_stocks(products):
    low_stock_products = []
    for product in products:
        if product["stock"]<= 2:
            low_stock_products.append(product)
    return low_stock_products
     

     
