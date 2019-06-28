import pytest
from django.test import Client
from django.contrib.auth.models import User
from consultations.models.emergency_care import Call, Triage
from consultations.models.patient import Patient
from users.models import Clerk, Medic


@pytest.fixture
def client():
    yield Client()

def test_homepage_unlogged(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_homepage_medic(client):
    medic = Medic.objects.create(username='test_user')
    medic.set_password('123')
    medic.save()

    client.force_login(medic)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/chamada-de-pacientes/'
    assert response.status_code == 302

@pytest.mark.django_db
def test_homepage_clerk(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/registro-de-pacientes/'
    assert response.status_code == 302

@pytest.mark.django_db
def test_homepage_superuser(client):
    user = User.objects.create(username='test_user')
    user.set_password('123')
    user.is_superuser = True
    user.save()

    client.force_login(user)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_patient_register_risk_level_0(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 0
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/registro-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/registro-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_patient_register_risk_level_1(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 1
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/registro-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/registro-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_patient_register_risk_level_2(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 2
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/registro-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/registro-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_patient_register_risk_level_3(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 3
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/registro-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/registro-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_patient_call_risk_level_0(client):
    medic = Medic.objects.create(username='test_user')
    medic.set_password('123')
    medic.save()

    client.force_login(medic)

    patient_data = {
        "first_name": "João",
        "last_name": "Cardoso de Almeida",
        "birthdate": "1990-01-01T00:00:00Z",
        "gender": "M",
        "id_document": "static/images/document.jpg",
        "identification": "13034595077",
        "telefone_numbers": "{\"fixo\": \"36001234\", \"celular\": \"991001234\"}",
        "email": "joao@gmail.com",
        "health_insurance": "123",
        "health_insurance_document": "static/images/document2.png"
    }

    patient = Patient.objects.create(**patient_data)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 0,
        "patient_id": patient.id
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/chamada-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/chamada-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_patient_call_risk_level_1(client):
    medic = Medic.objects.create(username='test_user')
    medic.set_password('123')
    medic.save()

    client.force_login(medic)

    patient_data = {
        "first_name": "João",
        "last_name": "Cardoso de Almeida",
        "birthdate": "1990-01-01T00:00:00Z",
        "gender": "M",
        "id_document": "static/images/document.jpg",
        "identification": "13034595077",
        "telefone_numbers": "{\"fixo\": \"36001234\", \"celular\": \"991001234\"}",
        "email": "joao@gmail.com",
        "health_insurance": "123",
        "health_insurance_document": "static/images/document2.png"
    }

    patient = Patient.objects.create(**patient_data)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 1,
        "patient_id": patient.id
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/chamada-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/chamada-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_patient_call_risk_level_2(client):
    medic = Medic.objects.create(username='test_user')
    medic.set_password('123')
    medic.save()

    client.force_login(medic)

    patient_data = {
        "first_name": "João",
        "last_name": "Cardoso de Almeida",
        "birthdate": "1990-01-01T00:00:00Z",
        "gender": "M",
        "id_document": "static/images/document.jpg",
        "identification": "13034595077",
        "telefone_numbers": "{\"fixo\": \"36001234\", \"celular\": \"991001234\"}",
        "email": "joao@gmail.com",
        "health_insurance": "123",
        "health_insurance_document": "static/images/document2.png"
    }

    patient = Patient.objects.create(**patient_data)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 2,
        "patient_id": patient.id
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/chamada-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/chamada-de-pacientes/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_patient_call_risk_level_3(client):
    medic = Medic.objects.create(username='test_user')
    medic.set_password('123')
    medic.save()

    client.force_login(medic)

    patient_data = {
        "first_name": "João",
        "last_name": "Cardoso de Almeida",
        "birthdate": "1990-01-01T00:00:00Z",
        "gender": "M",
        "id_document": "static/images/document.jpg",
        "identification": "13034595077",
        "telefone_numbers": "{\"fixo\": \"36001234\", \"celular\": \"991001234\"}",
        "email": "joao@gmail.com",
        "health_insurance": "123",
        "health_insurance_document": "static/images/document2.png"
    }

    patient = Patient.objects.create(**patient_data)

    triage_data = {
        "body_temperature": 38.2,
        "body_mass": 110.75,
        "name": "João",
        "age": 25,
        "blood_pressure": "[\"120\", \"81\"]",
        "blood_oxygen_level": 90.0,
        "main_complaint": "[\"Dor de cabeca\", \"Enjoo\", \"Vomito\"]",
        "alergies": "[\"Dipirona\", \"Amoxilina\"]",
        "continuos_medication": "[\"Colaxalozam\", \"Alprazolam\"]",
        "previous_diagnosis": "[\"Enxaqueca\"]",
        "height": 1.75,
        "risk_level": 3,
        "patient_id": patient.id
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/autenticacao/efetuar-login/')

    assert response.url == '/'
    assert response.status_code == 302

    response = client.get('/')

    assert response.url == '/chamada-de-pacientes/'
    assert response.status_code == 302

    response = client.get('/chamada-de-pacientes/')

    assert response.status_code == 200

def test_calls_page(client):
    response = client.get('/chamadas/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_check_calls_changes(client):
    Call.objects.create(location='test')
    
    response = client.get('/chamadas/checar-mudancas/')

    assert response.status_code == 200
