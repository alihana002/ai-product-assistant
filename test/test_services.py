from ai_product_assistant.services import delete_product



def test_delete_existing_product():
    product_list = [
        {
            "id": 1,
            "name": "Tisch",
            "stock": 2,
            "price": 200
        },

        {
                    "id": 2,
                    "name": "Couch",
                    "stock": 2,
                    "price": 300
                }
    ]


    result = delete_product(1, product_list)

    assert result == "product deleted"
    """
    geht damit, das ist list comprehension (ids var), krürzer. 
    wie geht mit normaler funktiom?
    """
    ids = [product["id"] for product in product_list]

    assert 1 not in ids;
    assert 2 in ids;




    def test_delete_not_existing_product():
        product_list = [
            {
                "id": 1,
                "name": "Tisch",
                "stock": 2,
                "price": 200
            },

            {
                        "id": 2,
                        "name": "Couch",
                        "stock": 2,
                        "price": 300
                    }
        ]

        ids_before = [product["id"] for product in product_list]
        result = delete_product(99, product_list)
        ids_now  = [product["id"] for product in product_list]
    

        assert result is None 

        assert ids_before == ids_now

        

