import requests
import time

def test_get_domains():
    #API URL
    baseUrl = "https://reqres.in/api"
    url = baseUrl + "/users/1"
    
    # Read json file
    file = open('userUpdated.json','r')
    body = file.read()

    #API call
    start = time.time()    
    put_response = requests.put(url,body)
    roundtrip = time.time() - start

    # Verify status code
    assert put_response.status_code == 200

    # Verify content-type
    assert put_response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure (Assuming a 'total_page' in data and value 2)
    data = put_response.json()
    assert isinstance(data,dict)
    assert "updatedAt" in data

    # Verify response response time is equal or less than 2ms
    assert roundtrip <= 2