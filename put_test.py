import requests
import time

def put_user():
    #API URL
    baseUrl = "https://reqres.in/api"
    url = baseUrl + "/users/1"

    # Read json file
    file = open('userUpdated.json','r')
    body = file.read()

    #API call
    start = time.time()    
    response = requests.put(url,body)
    roundtrip = time.time() - start

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure (Assuming a 'updatedAt' in data)
    data = response.json()
    assert isinstance(data,dict)
    assert "updatedAt" in data

    # Verify response response time is equal or less than 2ms
    assert roundtrip <= 2