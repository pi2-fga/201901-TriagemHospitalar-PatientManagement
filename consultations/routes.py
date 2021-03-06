import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from boogie.router import Router
from consultations import models
from consultations.forms import PatientRegistrationForm, ConsultationForm
from consultations.models import Triage, Consultation, Patient, Call
import numpy
import json

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
        triage_information['risk']['background_color'] = \
            Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]
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

            form = PatientRegistrationForm(
                request.POST or None,
                request.FILES or None
            )

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
                    'patient_registration.html',
                    {
                        'form': form,
                        'triage_information': triage_information
                    }
                )

        if request.method == 'GET':

            if triage.patient is None:

                Call.objects.create(
                    clerk=request.user.clerk,
                    patient_name=triage.name,
                    location=request.user.clerk.window
                )

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


@urlpatterns.route('cadastrar/' + triage_url + 'atualizar-existente/' +
                   patient_url)
def patient_registration_change_patient_data(request, triage, patient):
    """
    [...]
    """

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

        triage_information = dict()
        triage_information['name'] = triage.name
        triage_information['age'] = triage.age
        triage_information['risk'] = dict()
        triage_information['risk']['background_color'] = \
            Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]
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

            form = PatientRegistrationForm(
                request.POST or None,
                request.FILES or None,
                instance=patient
            )

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
            patient_dict['telefone_number'] = \
                patient.get_telefone_numbers()['fixo']
            patient_dict['cellphone_number'] = \
                patient.get_telefone_numbers()['celular']
            patient_dict['email'] = patient.email
            patient_dict['health_insurance'] = patient.health_insurance
            patient_dict['id_document'] = patient.id_document
            patient_dict['health_insurance_document'] = \
                patient.health_insurance_document

            patient_documents = dict()
            patient_documents['id_document'] = \
                patient.id_document.name.replace('static/images/', '')
            patient_documents['health_insurance_document'] = \
                patient.health_insurance_document.name.replace(
                    'static/images/',
                    ''
                )

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

            form = PatientRegistrationForm(
                request.POST or None,
                request.FILES or None,
                instance=patient
            )

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
            patient_dict['telefone_number'] = \
                patient.get_telefone_numbers()['fixo']
            patient_dict['cellphone_number'] = \
                patient.get_telefone_numbers()['celular']
            patient_dict['email'] = patient.email
            patient_dict['health_insurance'] = patient.health_insurance
            patient_dict['id_document'] = patient.id_document
            patient_dict['health_insurance_document'] = \
                patient.health_insurance_document

            patient_documents = dict()
            patient_documents['id_document'] = \
                patient.id_document.name.replace('static/images/', '')
            patient_documents['health_insurance_document'] = \
                patient.health_insurance_document.name.replace(
                    'static/images/',
                    ''
                )

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

    if request.user.is_authenticated:

        search_term = request.GET.get('search')

        if search_term:

            result = Patient.objects.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term)
            )

            if hasattr(request.user, 'clerk'):
                user_type = 'clerk'
            elif hasattr(request.user, 'medic'):
                user_type = 'medic'
            else:
                user_type = 'admin'

            response = render(
                request,
                'patient_list.html',
                {
                    'patients': result,
                    'number': result.count(),
                    'user_type': user_type
                }
            )

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

            form = ConsultationForm(
                request.POST or None,
                instance=consultation
            )

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

            if consultation is None:

                Call.objects.create(
                    medic=request.user.medic,
                    patient=patient,
                    location=request.user.medic.room
                )

            form = ConsultationForm(instance=consultation)

            response = render(
                request,
                'patient_detail.html',
                {
                    'has_eletrocardiogram': triage.get_eletrocardiogram,
                    'form': form,
                    'patient': patient,
                    'triage': triage,
                    'triage_risk': triage_risk
                }
            )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('eletrocardiograma/' + patient_url)
def patient_eletrocardiogram(request, patient):
    """
    Renders a page with patient eletrocardiogram.
    """
    if hasattr(request.user, 'medic') or request.user.is_superuser:
        triage = patient.triages.last()
        if request.method == 'POST':
            response = redirect('/paciente/consulta/' + patient.pk)
        if request.method == 'GET':
            try:
                time = len(triage.get_eletrocardiogram()) / 128
            except TypeError:
                time = None
            x_list = list(numpy.arange(0, time, 0.0078125))
            response = render(
                request,
                'patient_eletrocardiogram.html',
                {
                    'patient': patient,
                    'triage': triage,
                    'eletrocardiogram': triage.get_eletrocardiogram(),
                    'time': x_list
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
        received_json_data = json.loads(data)
        triage = Triage.objects.create(**received_json_data['triage'])
        triage.save()

        if type(triage.alergies) is not list:
            triage.alergies = json.dumps([triage.alergies])

        if type(triage.main_complaint) is not list:
            triage.main_complaint = json.dumps([triage.main_complaint])

        if type(triage.continuos_medication) is not list:
            triage.continuos_medication = \
                json.dumps([triage.continuos_medication])

        triage.save()

        return HttpResponse("Triagem salva com sucesso",
                            content_type="text/plain", status=200)
    return None
