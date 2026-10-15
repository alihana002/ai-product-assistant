from ai_product_assistant.repository import get_api_product
from ai_product_assistant.models import Product
from unittest.mock import Mock, patch
import requests
import pytest 

def test_get_api_products():

    api_product_dict = {
       "id": 1,
        "title": "couch",
        "price" : 200,
        "stock": 2       
    }
       
    expected_product : Product = Product (
        id =  api_product_dict["id"],
        name = api_product_dict["title"],
        price = api_product_dict["price"], 
        stock = api_product_dict["stock"]

    )


    fake_response = Mock()
    fake_response.json.return_value = api_product_dict
    fake_response.raise_for_status.return_value = None

    with patch(
        "ai_product_assistant.repository.requests.get",
        return_value=fake_response,
    ):
        result = get_api_product(1)
 

    assert expected_product == result



def test_get_api_product_404_error():

  
    
    
        fake_response = Mock()
        fake_response.status_code = 404
        fake_response.raise_for_status.side_effect = requests.HTTPError
    
        with patch(
            "ai_product_assistant.repository.requests.get",
            return_value=fake_response,
        ):
            result = get_api_product(999)

        
    
        assert result is None 




def test_get_api_product_500_error():

  
    
    
        fake_response = Mock()
        fake_response.status_code = 500
        fake_response.raise_for_status.side_effect = requests.HTTPError
    
        with patch(
        "ai_product_assistant.repository.requests.get",
        return_value=fake_response,
    ):
            with pytest.raises(requests.HTTPError):
                get_api_product(999)
            
            
    