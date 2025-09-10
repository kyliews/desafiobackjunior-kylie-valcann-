def test_get_users_success(client):
    """
    Testa se a rota GET /users retorna sucesso (200) e a estrutura esperada.
    """
    response = client.get('/users')
    json_data = response.get_json()

    assert response.status_code == 200
    assert 'data' in json_data
    assert 'pagination' in json_data
    assert isinstance(json_data['data'], list) 

def test_get_user_by_id_success(client):
    """
    Testa se a rota GET /users/<id> retorna um usuário existente.
    """
    response = client.get('/users/1') 
    json_data = response.get_json()

    assert response.status_code == 200
    assert 'data' in json_data
    assert json_data['data']['id'] == 1
    assert json_data['data']['name'] == 'joão Silva'

def test_get_user_by_id_not_found(client):
    """
    Testa se a rota GET /users/<id> retorna 404 para um usuário inexistente.
    """
    response = client.get('/users/999')

    assert response.status_code == 404
    json_data = response.get_json()
    assert 'error' in json_data
    assert json_data['error']['message'] == 'User not found'

def test_get_users_with_filters(client):
    """
    Testa os filtros 'role' e 'is_active'.
    """
    response = client.get('/users?role=analyst')
    json_data = response.get_json()

    assert response.status_code == 200
    for user in json_data['data']:
        assert user['role'] == 'analyst'
    
    response = client.get('/users?is_active=false')
    json_data = response.get_json()

    assert response.status_code == 200
    for user in json_data['data']:
        assert user['is_active'] is False

def test_get_users_search_query(client):
    """
    Testa a funcionalidade de busca com o parâmetro 'q'.
    """
    response = client.get('/users?q=hoffmann')
    json_data = response.get_json()

    assert response.status_code == 200
    assert len(json_data['data']) > 0 
    for user in json_data['data']:
        assert 'hoffmann' in user['name'].lower() or 'hoffmann' in user['email'].lower()

def test_get_users_pagination(client):
    """
    Testa a funcionalidade de paginação.
    """
    response = client.get('/users?page=1&page_size=1')
    json_data = response.get_json()

    assert response.status_code == 200
    assert len(json_data['data']) == 1 
    assert json_data['pagination']['current_page'] == 1
    assert json_data['pagination']['page_size'] == 1

def test_get_users_invalid_page_size(client):
    """
    Testa se um page_size muito grande retorna um erro 400.
    """
    response = client.get('/users?page_size=100')
    
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'error' in json_data
    assert "page_size cannot be greater than 50" in json_data['error']['message']
