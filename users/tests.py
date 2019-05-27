import pytest
from django.test import Client


@pytest.fixture
def client():
    yield Client()


def test_login_route(client):
    response = client.get('/autenticacao/efetuar-login/')
    assert response.status_code == 200
