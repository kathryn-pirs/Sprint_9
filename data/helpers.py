import json
import random
import string
import uuid
from urllib import request

_API_BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru/"


def generate_recipe_data(data):
    return random.choice(data)


def get_random_number():
    return str(random.randint(10000000, 90000000))


def generate_credentials():
    password = f"fsZ{str(uuid.uuid4())[:-30]}{get_random_number()}"
    name = f'Шеф{get_random_number()}'
    lastname = f'Шефский{get_random_number()}'
    username = f'test{get_random_number()}'
    email = f"{get_random_number()}@yandex.ru"
    return name, lastname, username, email, password


def is_backend_login_working():
    try:
        rand = ''.join(random.choices(string.digits, k=8))
        email = f'check{rand}@test.com'
        password = f'Test@123!{rand[:4]}'
        username = f'check_{rand}'
        api_base = _API_BASE_URL.rstrip('/')

        reg_data = json.dumps({
            'email': email, 'password': password, 'username': username,
            'first_name': 'Check', 'last_name': 'User'
        }).encode()
        req = request.Request(
            f'{api_base}/api/users/',
            data=reg_data,
            headers={'Content-Type': 'application/json'}
        )
        resp = request.urlopen(req, timeout=10)
        if resp.status != 201:
            return False

        login_data = json.dumps({
            'email': email, 'password': password
        }).encode()
        req2 = request.Request(
            f'{api_base}/api/auth/token/login/',
            data=login_data,
            headers={'Content-Type': 'application/json'}
        )
        resp2 = request.urlopen(req2, timeout=10)
        return resp2.status == 200
    except Exception:
        return False