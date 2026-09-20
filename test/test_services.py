from ai_product_assistant.services import delete_product, get_product_by_id
from ai_product_assistant.models import Product


def test_delete_existing_product():


    tisch = Product(1, "Tisch", 2, 200)
    couch = Product(2, "Couch", 3, 150)

    product_list = [tisch, couch]

    result = delete_product(1, product_list)
    print(result)
    

    assert result == "product deleted"
    """
    geht damit, das ist list comprehension (ids var), krürzer. 
    wie geht mit normaler funktiom?
    """
    

    assert tisch not in product_list ;
    assert couch in product_list;







        
def test_delete_not_existing_product():
       
        
        tisch = Product(1, "Tisch", 2, 200)
        couch = Product(2, "Couch", 3, 150)

        product_list = [tisch, couch]
        result = delete_product(99, product_list)
        print(result)
      
    

        assert result is None 


def test_get_product_by_id():
             
        tisch = Product(1, "Tisch", 2, 200)
        couch = Product(2, "Couch", 3, 150)

        product_list = [tisch, couch]
        result = get_product_by_id(1, product_list)
        assert result == tisch 
        print(result)



      
def test_get_not_existing_product_by_id():
        tisch = Product(1, "Tisch", 2, 200)
        couch = Product(2, "Couch", 3, 150)
       
        product_list = [tisch, couch]
        result = get_product_by_id(99, product_list)

        print(result)
        assert result is None 

