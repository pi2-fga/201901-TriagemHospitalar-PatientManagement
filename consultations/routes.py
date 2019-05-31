import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from boogie.router import Router
from consultations import models
from consultations.forms import PatientRegistrationForm, ConsultationForm
from consultations.models import Triage, Consultation, Patient

app_name = 'consultations'
urlpatterns = Router(
    models={
        'triage': Triage,
        'patient': Patient,
    },
    lookup_field={
        'triage': 'pk',
    },
)
triage_url = f'<model:triage>/'
patient_url = f'<model:patient>/'


@urlpatterns.route('cadastrar/' + triage_url)
def patient_registration(request, triage):
    """
    Renders a page with PatientRegistrationForm
    """

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

        triage_information = dict()
        triage_information['name'] = triage.name
        triage_information['age'] = triage.age
        triage_information['risk'] = dict()
        triage_information['risk']['background_color'] = Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]
        if triage.risk_level == 0:
            triage_information['risk']['text'] = 'VERMELHO'
            triage_information['risk']['text_color'] = 'white'
        elif triage.risk_level == 1:
            triage_information['risk']['text'] = 'AMARELO'
            triage_information['risk']['text_color'] = 'black'

        elif triage.risk_level == 2:
            triage_information['risk']['text'] = 'VERDE'
            triage_information['risk']['text_color'] = 'white'
        elif triage.risk_level == 3:
            triage_information['risk']['text'] = 'AZUL'
            triage_information['risk']['text_color'] = 'white'

        if request.method == 'POST':

            form = PatientRegistrationForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                patient = form.save()
                triage.patient = patient
                triage.save()
                response = redirect('/')

            else:
                response = render(
                    request,
                    'patient_registration.html',
                    {
                        'form': form,
                        'triage_information': triage_information
                    }
                )

        if request.method == 'GET':

            result = Patient.objects.all()

            patients_dict = dict()
            patients_dict['patients'] = list()

            for patient in result:

                patient_dict = dict()
                patient_dict['id'] = patient.id
                patient_dict['first_name'] = patient.first_name
                patient_dict['last_name'] = patient.last_name
                patient_dict['birthdate'] = patient.birthdate.date

                patients_dict['patients'].append(patient_dict)

            patients_dict['count'] = result.count()

            form = PatientRegistrationForm()

            response = render(
                request,
                'patient_registration.html',
                {
                    'form': form,
                    'triage_information': triage_information,
                    'patients_dict': patients_dict
                }
            )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('cadastrar/' + triage_url + 'usar-existente/' + patient_url)
def patient_registration_keep_patient_data(request, triage, patient):
    """
    [...]
    """

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

        if request.method == 'GET':

            triage.patient = patient
            triage.save()

            response = redirect('/')

    else:

        response = redirect('/')

    return response


@urlpatterns.route('cadastrar/' + triage_url + 'atualizar-existente/' + patient_url)
def patient_registration_change_patient_data(request, triage, patient):
    """
    [...]
    """

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

        triage_information = dict()
        triage_information['name'] = triage.name
        triage_information['age'] = triage.age
        triage_information['risk'] = dict()
        triage_information['risk']['background_color'] = Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]
        if triage.risk_level == 0:
            triage_information['risk']['text'] = 'VERMELHO'
            triage_information['risk']['text_color'] = 'white'
        elif triage.risk_level == 1:
            triage_information['risk']['text'] = 'AMARELO'
            triage_information['risk']['text_color'] = 'black'

        elif triage.risk_level == 2:
            triage_information['risk']['text'] = 'VERDE'
            triage_information['risk']['text_color'] = 'white'
        elif triage.risk_level == 3:
            triage_information['risk']['text'] = 'AZUL'
            triage_information['risk']['text_color'] = 'white'

        if request.method == 'POST':

            form = PatientRegistrationForm(request.POST or None, request.FILES or None, instance=patient)

            if form.is_valid():

                patient = form.save()
                patient.email = request.POST['email']
                patient.save()
                triage.patient = patient
                triage.save()
                response = redirect('/')

            else:
                response = render(
                    request,
                    'patient_update_triage.html',
                    {
                        'form': form,
                        'triage_information': triage_information
                    }
                )

        if request.method == 'GET':

            patient_dict = dict()
            patient_dict['first_name'] = patient.first_name
            patient_dict['last_name'] = patient.last_name
            patient_dict['identification'] = patient.identification
            patient_dict['birthdate'] = patient.birthdate.strftime('%Y-%m-%d')
            patient_dict['gender'] = patient.gender
            patient_dict['telefone_number'] = patient.get_telefone_numbers()['fixo']
            patient_dict['cellphone_number'] = patient.get_telefone_numbers()['celular']
            patient_dict['email'] = patient.email
            patient_dict['health_insurance'] = patient.health_insurance
            patient_dict['id_document'] = patient.id_document
            patient_dict['health_insurance_document'] = patient.health_insurance_document

            patient_documents = dict()
            patient_documents['id_document'] = \
                patient.id_document.name.replace('static/images/', '')
            patient_documents['health_insurance_document'] = \
                patient.health_insurance_document.name.replace('static/images/', '')

            form = PatientRegistrationForm(patient_dict)

            response = render(
                request,
                'patient_update_triage.html',
                {
                    'form': form,
                    'triage_information': triage_information,
                    'patient_documents': patient_documents
                }
            )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('atualizar/' + patient_url)
def patient_update(request, patient):
    """
    Renders a page with PatientRegistrationForm
    """

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

        if request.method == 'POST':

            form = PatientRegistrationForm(request.POST or None, request.FILES or None, instance=patient)

            if form.is_valid():

                patient = form.save()
                patient.email = request.POST['email']
                patient.save()
                response = redirect('/')

            else:
                response = render(
                    request,
                    'patient_update.html',
                    {
                        'form': form
                    }
                )

        if request.method == 'GET':

            patient_dict = dict()
            patient_dict['first_name'] = patient.first_name
            patient_dict['last_name'] = patient.last_name
            patient_dict['identification'] = patient.identification
            patient_dict['birthdate'] = patient.birthdate.strftime('%Y-%m-%d')
            patient_dict['gender'] = patient.gender
            patient_dict['telefone_number'] = patient.get_telefone_numbers()['fixo']
            patient_dict['cellphone_number'] = patient.get_telefone_numbers()['celular']
            patient_dict['email'] = patient.email
            patient_dict['health_insurance'] = patient.health_insurance
            patient_dict['id_document'] = patient.id_document
            patient_dict['health_insurance_document'] = patient.health_insurance_document

            patient_documents = dict()
            patient_documents['id_document'] = \
                patient.id_document.name.replace('static/images/', '')
            patient_documents['health_insurance_document'] = \
                patient.health_insurance_document.name.replace('static/images/', '')

            form = PatientRegistrationForm(patient_dict)

            response = render(
                request,
                'patient_update.html',
                {
                    'form': form,
                    'patient_documents': patient_documents
                }
            )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('lista/')
def list_patient_search(request):

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

        search_term = request.GET.get('search')
        if search_term:
            result = Patient.objects.filter(Q(first_name__icontains=search_term) |
                                            Q(last_name__icontains=search_term))
            response = render(request, 'patient_list.html',
                        {'patients': result, 'number': result.count()})

    else:

        response = redirect('/')

    return response


@urlpatterns.route('consulta/' + patient_url)
def patient_detail(request, patient):
    """
    Renders a page with patient and their triage information, as well as
    a ConsultationForm for a medic to fill with information.
    TODO: Add validation to form and medic permission to this page.
    """

    if hasattr(request.user, 'medic') or request.user.is_superuser:

        triage = patient.triages.last()

        consultation = Consultation.objects.filter(triage=triage)

        if consultation and len(consultation) == 1:
            consultation = consultation[0]
        else:
            consultation = None

        triage_risk = dict()
        triage_risk['background_color'] = \
            Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]

        if triage.risk_level == 0:
            triage_risk['text'] = 'VERMELHO'
            triage_risk['text_color'] = 'white'
        elif triage.risk_level == 1:
            triage_risk['text'] = 'AMARELO'
            triage_risk['text_color'] = 'black'

        elif triage.risk_level == 2:
            triage_risk['text'] = 'VERDE'
            triage_risk['text_color'] = 'white'
        elif triage.risk_level == 3:
            triage_risk['text'] = 'AZUL'
            triage_risk['text_color'] = 'white'

        if request.method == 'POST':

            form = ConsultationForm(request.POST or None, instance=consultation)

            if form.is_valid():
                consultation = form.save(commit=False)
                consultation.medic = request.user.medic
                consultation.triage = triage
                consultation.save()

                response = redirect('/')

            else:
                response = render(
                    request,
                    'patient_detail.html',
                    {
                        'form': form,
                        'patient': patient,
                        'triage': triage,
                        'triage_risk': triage_risk
                    }
                )

        if request.method == 'GET':

            form = ConsultationForm(instance=consultation)

            response = render(
                request,
                'patient_detail.html',
                {
                    'form': form,
                    'patient': patient,
                    'triage': triage,
                    'triage_risk': triage_risk
                }
            )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('consultas/' + patient_url)
def list_patient_consultations(request, patient):
    """
    Renders a page with patient and their triage information, as well as
    a ConsultationForm for a medic to fill with information.
    TODO: Add validation to form and medic permission to this page.
    """

    if hasattr(request.user, 'medic') or request.user.is_superuser:

        consultations = Consultation.objects.filter(
            triage__patient=patient
        )

        response = render(
            request,
            'patient_consultations_list.html',
            {
                'consultations': consultations,
                'patient': patient
            }
        )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('triagem/', csrf=False)
def triage_information(request):
    """
    Process triage information sent from a json and saves it to database
    """
    print(request.body)
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        print('dataaaaaaaaaaaaaaaaaa')
        print(data)
        received_json_data = json.loads(data)
        print(received_json_data['triage'])
        print('received_json_data')
        triage = Triage.objects.create(**received_json_data['triage'])
        triage.save()
        return HttpResponse(triage, status_code=200)
    return None
