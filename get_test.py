import requests
import time

def get_users():
    #Functionality  testing

    #API URL
    baseUrl = "https://reqres.in/api"
    url = baseUrl + "/users?page=2"

    #API call
    start = time.time()
    response = requests.get(url)
    roundtrip = time.time() - start

    # Verify status code
    assert response.status_code == 200 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure (Assuming a 'total_page' in data and value 2)
    data = response.json()
    assert isinstance(data,dict)
    assert "total_pages" in data
    assert data["total_pages"] == 2

    # Verify response response time is equal or less than 2ms
    assert roundtrip <= 2