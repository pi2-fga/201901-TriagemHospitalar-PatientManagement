import pytest
from django.test import Client
from django.contrib.auth.models import User
from consultations.models.emergency_care import Call, Triage
from consultations.models.patient import Patient
from users.models import Clerk, Medic


@pytest.fixture
def client():
    yield Client()

@pytest.mark.django_db
def test_call_create(client):
    call_1 = Call.objects.create()
    call_1.__str__()

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

    clerk = Clerk.objects.create(username='test_user1')
    clerk.set_password('123')
    clerk.save()
    call_2 = Call.objects.create(clerk=clerk, patient_name=patient_data['first_name'])
    call_2.__str__()

    medic = Medic.objects.create(username='test_user2')
    medic.set_password('123')
    medic.save()
    call_3 = Call.objects.create(medic=medic, patient=patient)
    call_3.__str__()

    assert call_1 is not None
    assert call_2 is not None
    assert call_3 is not None

@pytest.mark.django_db
def test_clerk_register_risk_level_0(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 0
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_risk_level_1(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 1
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_risk_level_2(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 2
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_risk_level_3(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 3
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_post(client):
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

    response = client.post('/paciente/cadastrar/' + str(triage.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_existing_patient(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 0
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) +
                          '/usar-existente/' + str(patient.id) + '/')

    assert response.url == '/'
    assert response.status_code == 302

@pytest.mark.django_db
def test_clerk_register_updating_existing_patient_risk_level_0(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 0
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) +
                          '/atualizar-existente/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_updating_existing_patient_risk_level_1(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 1
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) +
                          '/atualizar-existente/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_updating_existing_patient_risk_level_2(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 2
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) +
                          '/atualizar-existente/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_updating_existing_patient_risk_level_3(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 3
    }

    triage = Triage.objects.create(**triage_data)

    response = client.get('/paciente/cadastrar/' + str(triage.id) +
                          '/atualizar-existente/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_register_updating_existing_patient_post(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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
        "risk_level": 0
    }

    triage = Triage.objects.create(**triage_data)

    response = client.post('/paciente/cadastrar/' + str(triage.id) +
                          '/atualizar-existente/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_update_patient(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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

    response = client.get('/paciente/atualizar/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_update_patient_post(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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

    response = client.post('/paciente/atualizar/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_clerk_search(client):
    clerk = Clerk.objects.create(username='test_user')
    clerk.set_password('123')
    clerk.save()

    client.force_login(clerk)

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

    response = client.get('/paciente/lista/?search=joão')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_consultation_risk_level_0(client):
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

    response = client.get('/paciente/consulta/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_consultation_risk_level_1(client):
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

    response = client.get('/paciente/consulta/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_consultation_risk_level_2(client):
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

    response = client.get('/paciente/consulta/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_consultation_risk_level_3(client):
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

    response = client.get('/paciente/consulta/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_consultation_post(client):
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

    response = client.post('/paciente/consulta/' + str(patient.id) + '/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_medic_list_consultations(client):
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

    response = client.get('/paciente/consultas/' + str(patient.id) + '/')

    assert response.status_code == 200
