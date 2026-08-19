def main() -> None:
    while True:
        try:
            product_id = int(input("Welche id? "))
        except ValueError:
            print("Es wird eine Zahl erwartet")
            continue

        product = get_product(product_id)
        print(f"Name: {product["name"]}")
        print(f"Preis: {product["price"]}")

products = [
    {"id": 1, "name": "Tisch", "price": 299},
    {"id": 2, "name": "Stuhl", "price": 99},
    {"id": 3, "name": "Schrank", "price": 599}
]



def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return f"Kein Produkt mit der Id gefunden"