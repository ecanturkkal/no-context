def test_read_todos(test_client):
    response = test_client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo(test_client):
    response = test_client.post("/todos", json={"name": "Buy groceries", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}

def test_read_todo(test_client):
    test_client.post("todos/", json={"name": "Buy groceries", "completed": False})
    response = test_client.get("todos/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}

def test_update_todo(test_client):
    test_client.post("todos/", json={"name": "Buy groceries", "completed": False})
    response = test_client.put("todos/1", json={"name": "Buy vegetables", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy vegetables", "completed": True}

def test_delete_todo(test_client):
    test_client.post("todos/", json={"name": "Buy groceries", "completed": False})
    response = test_client.delete("todos/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}