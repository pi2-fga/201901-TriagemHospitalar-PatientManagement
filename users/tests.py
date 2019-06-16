import pytest
from django.test import Client
from django.contrib.auth.models import User


@pytest.fixture
def client():
    yield Client()

def test_login_route(client):
    response = client.get('/autenticacao/efetuar-login/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_route_already_logged(client):

    user = User.objects.create(username='test_user')
    user.set_password('123')
    user.save()

    client.force_login(user)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

@pytest.mark.django_db
def test_login(client):

    user = User.objects.create(username='test_user')
    user.set_password('123')
    user.save()

    user_data = {
        'username': 'test_user',
        'password': '123'
    }

    response = client.post(
        '/autenticacao/efetuar-login/',
        user_data
    )

    assert response.url == '/'
    assert response.status_code == 302

@pytest.mark.django_db
def test_login_failed(client):

    user = User.objects.create(username='test_user')
    user.set_password('123')
    user.save()

    user_data = {
        'username': 'test_user',
        'password': 'wrong_pass'
    }

    response = client.post(
        '/autenticacao/efetuar-login/',
        user_data
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_sign_out(client):

    user = User.objects.create(username='test_user')
    user.set_password('123')
    user.save()

    user_data = {
        'username': 'test_user',
        'password': '123'
    }

    response = client.post(
        '/autenticacao/efetuar-login/',
        user_data
    )

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/autenticacao/encerrar-sessao/')

    assert response.url == '/'
    assert response.status_code == 302
