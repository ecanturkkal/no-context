def test_say_hello(test_client):
    response = test_client.get("hello_world/My name")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello My name"}