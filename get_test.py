import requests


def test_get_pokemon_by_name():
    #Functionality  testing
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure (Assuming a book object with 'id', 'title', and 'author')
    data = response.json()  
    assert isinstance(data, dict)
    assert "abilities" in data
    assert "name" in data