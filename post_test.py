import requests
import time

def post_user():
    #API URL
    baseUrl = "https://reqres.in/api"
    url = baseUrl + "/users"
    # Read json file
    file = open('newUser.json','r')
    body = file.read()

    #API call
    start = time.time()
    response = requests.post(url,body)
    roundtrip = time.time() - start

    # Verify status code
    assert response.status_code == 201

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure (Assuming a 'id' in data)
    data = response.json()
    assert isinstance(data,dict)
    assert "id" in data

    # Verify response response time is equal or less than 2ms
    assert roundtrip <= 2