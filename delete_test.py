import requests
import time

def delete_user():
    #API URL
    baseUrl = "https://reqres.in/api"
    url = baseUrl + "/users/1"

    #API call
    start = time.time()    
    response = requests.delete(url)
    roundtrip = time.time() - start

    # Verify status code
    assert response.status_code == 204

    # Veriy no content is send
    assert response.text == ""
    # Verify response response time is equal or less than 2ms
    assert roundtrip <= 2