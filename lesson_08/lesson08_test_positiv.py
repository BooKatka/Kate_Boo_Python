import pytest
import json
import requests


# GET-запрос
@pytest.fixture(scope="module")
def get_token():
    auth_data = {
        "login": "",
        "password": "",
        "companyId": ""  
    }

    headers = {'Content-Type': 'application/json'
               'Authorization': f'Bearer 1748757553785_50f0e10c25f740275536455d77ad9a4218d67fb67ad6dd882b35d4ea06ecf94f'} 

# POST-запрос на сервер для получения ключа авторизации
    response = requests.post(
        'https://ru.yougile.com/api-v2/auth/keys',
        data=json.dumps(auth_data),  
        headers=headers              
    )
    token = response.json()['key']
    yield token
    

# PUT -запрос через редактирование существующего проекта   
def test_edit_project(get_token):
    edit_data = {
        "deleted": False,             
        "title": "Проект_23",    # Новое название проекта
        "users": {                    
            'ff02d87a-5e23-4082-971d-d1f2ae3edf86': "admin"
        }
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer 1748757553785_50f0e10c25f740275536455d77ad9a4218d67fb67ad6dd882b35d4ea06ecf94f'}

# PUT-запрос для обновления проекта
    response = requests.put(
        'https://ru.yougile.com/api-v2/projects/'
        '37f070f0-6503-4f9e-9ba3-20c080f351d1',
        data=json.dumps(edit_data), headers=headers                 
    )
    
    print(response.json())

    assert response.status_code == 200

def get_projects_list(get_token):
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer 1748757553785_50f0e10c25f740275536455d77ad9a4218d67fb67ad6dd882b35d4ea06ecf94f'}

# GET-запрос для получения списка проектов
    response = requests.get(
        'https://ru.yougile.com/api-v2/projects',
        headers=headers
    )
    print(response.json())  
    get_projects_list('')
