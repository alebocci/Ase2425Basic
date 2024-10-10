import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_valid(client):
    response = client.get('/add?a=10&b=5')
    assert response.status_code == 200
    assert response.json['s'] == 15.0

def test_add_invalid(client):
    response = client.get('/add?a=10')
    assert response.status_code == 400
    assert b'Invalid input' in response.data

def test_sub_valid(client):
    response = client.get('/sub?a=10&b=5')
    assert response.status_code == 200
    assert response.json['s'] == 5.0

def test_sub_invalid(client):
    response = client.get('/sub?a=10')
    assert response.status_code == 400
    assert b'Invalid input' in response.data

def test_mul_valid(client):
    response = client.get('/mul?a=10&b=5')
    assert response.status_code == 200
    assert response.json['s'] == 50.0

def test_mul_invalid(client):
    response = client.get('/mul?a=10')
    assert response.status_code == 400
    assert b'Invalid input' in response.data

def test_div_valid(client):
    response = client.get('/div?a=10&b=5')
    assert response.status_code == 200
    assert response.json['s'] == 2.0

def test_div_by_zero(client):
    response = client.get('/div?a=10&b=0')
    assert response.status_code == 400
    assert b'Division by zero' in response.data

def test_concat_valid(client):
    response = client.get('/concat?a=hello&b=world')
    assert response.status_code == 200
    assert response.json['s'] == 'helloworld'

def test_concat_invalid(client):
    response = client.get('/concat?a=hello')
    assert response.status_code == 400
    assert b'Invalid input' in response.data

def test_rand_valid(client):
    response = client.get('/random?a=1&b=10')
    assert response.status_code == 200
    assert 1 <= response.json['s'] <= 10

def test_rand_invalid(client):
    response = client.get('/random?a=10&b=1')
    assert response.status_code == 400
    assert b'Invalid input' in response.data

def test_upper_valid(client):
    response = client.get('/upper?a=hello')
    assert response.status_code == 200
    assert response.json['s'] == 'HELLO'

def test_lower_valid(client):
    response = client.get('/lower?a=HELLO')
    assert response.status_code == 200
    assert response.json['s'] == 'hello'

def test_reduce_add(client):
    response = client.get('/reduce?op=add&lst=[1,2,3,4]')
    assert response.status_code == 200
    assert response.json['s'] == 10

def test_reduce_invalid_operator(client):
    response = client.get('/reduce?op=invalid&lst=[1,2,3]')
    assert response.status_code == 400
    assert b'Invalid operator' in response.data