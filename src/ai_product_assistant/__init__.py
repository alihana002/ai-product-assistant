
from .services import * 
from .repository import * 

def main() -> None:
    


    products = load_products()
  


    while True:

        

        print("\n--- Main Menu ---")
        print("1. get product (by id)")
        print("2. list products")
        print("3. search product")
        print("4. add product")
        print("5. update stock")
        print("6. get low stocks")
        print("7. delete product")
        print("8. Exit")


        choice = int(input("Enter your choice (1-8): "))


        if choice == 8:
            print("Exiting the program. Goodbye!")
            break  
    
        if choice == 1:
    
            while True:
                try:
                    product_id = int(input("Which id? "))
                except ValueError:
                    print("Integer is expected")
                    continue
                
                product = get_product_by_id(product_id, products)
                
                if product is None:
                    print("Id does not exist")
                else:
                    print(f"Name: {product.name}")
                    print(f"Preis: {product.price}")
                    break

            

        
        if choice == 2:
             
            product_list = list_products(products)
            print(f"those products exist: {product_list}")

            print("Do you want to select a product?")

            user_input = input("")

            if user_input.lower() == "yes":

                product_name = (input("Choose youre product: "))
                product = search_product(product_name, products)
                if product is None:
                    print("Product does not exist")
                else:
                     print(product)
            else:
                 print("Programm closed")

        if choice == 3:
                name = input("Enter product: ")
                found_product = search_product(name, products)
               
                if found_product is None:
                    print("Product does not exist")

                else:
                    print(f"Product found: {found_product.name}, {found_product.price}")

                

        if choice == 4:
             
    
            while True:
                try:
                    product_id = int(input("New id: "))
                except ValueError:
                    print("Integer is expected")
                    continue
                
            

                id_exist = get_product_by_id(product_id, products)
              
                if id_exist is not None:
                    print("id already exists")
                    continue
                break 


            name = input("enter a name: ")
            while True:
                try:
                    price = int(input("A price: "))
                    break
                except ValueError:
                    print("Integer is expected")
                    continue
                
            while True:
                    try:
                        stock = int(input("Youre Stock: "))
                        break 
                    except ValueError:
                        print("Integer is expected: ")
                        continue
             
            
            new_product = add_product(product_id, name, price, stock, products)
            save_products(products)
            print(f"Neues Produkt: {new_product}")
        

    
    
        if choice == 5:
    
        
                while True:
                            try:
                                input_product_id = int(input("Enter a productid for updating stock: "))
                            except ValueError:
                                print("You need to enter a number")
                                continue             

                            product = get_product_by_id(input_product_id, products)
                            
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
                            
                            

                            update_product = update_stock(input_product_id, input_stock, products)
                        
                            save_products(products)
                            print(update_product)
                        
                                
                            break
                
                


        if choice == 6:

            low_stock_list = get_low_stocks(products)
            if not low_stock_list:
                 print("No product with 2 or lower")
            else:
                print(low_stock_list)
        

        if choice == 7:
            delete_id = int(input("enter id from product: "))
            result = delete_product(delete_id, products)
            if result is None:
                print("id does not exist")


                save_products(products)
            
            print(result)
            print(products)

 
    



  
          


    
     
if __name__ == "__main__":
    main()