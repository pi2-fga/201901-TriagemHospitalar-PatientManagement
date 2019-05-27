import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from boogie.router import Router
from consultations import models
from consultations.forms import PatientRegistrationForm, ConsultationForm
from consultations.models import Triage, Consultation

app_name = 'consultations'
urlpatterns = Router(
    models={
        'triage': Triage,
        'patient_triage': models.PatientTriage,
    },
    lookup_field={
        'patient_triage': 'pk',
        'triage': 'pk',
    },
)
patient_triage_url = f'<model:patient_triage>/'
triage_url = f'<model:triage>/'


@urlpatterns.route('consulta/' + patient_triage_url)
def patient_detail(request, patient_triage):
    """
    Renders a page with patient and their triage information, as well as
    a ConsultationForm for a medic to fill with information.
    TODO: Add validation to form and medic permission to this page.
    """
    form = ConsultationForm
    return render(request, 'patient_detail.html',
                  {'form': form, 'patient': patient_triage.patient,
                   'triage': patient_triage.triage})


@urlpatterns.route('cadastrar/' + triage_url)
def patient_registration(request, triage):
    """
    Renders a page with PatientRegistrationForm
    """
    form = PatientRegistrationForm()

    if request.method == 'POST':
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            models.PatientTriage.objects.create(patient=patient, triage=triage)
            return redirect('/')
    risk_color = Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]
    return render(request, 'patient_registration.html',
                  {'form': form,
                   'risk_color': risk_color})


@urlpatterns.route('consultas/' + patient_triage_url)
def list_patient_consultations(request, patient_triage):
    """
    Renders a page with patient and their triage information, as well as
    a ConsultationForm for a medic to fill with information.
    TODO: Add validation to form and medic permission to this page.
    """
    consultations = (Consultation.objects
                     .filter(patient_triage__patient=patient_triage.patient))
    return render(request, 'patient_consultations_list.html',
                  {'consultations': consultations,
                   'patient_triage': patient_triage})


@csrf_exempt
@urlpatterns.route('triagem/')
def triage_information(request):
    """
    Process triage information sent from a json and saves it to database
    """
    print(request.body)
    if request.METHOD == 'POST':
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        print(received_json_data)
        triage = Triage.objects.create(received_json_data['triage'])
        triage.save()
        return HttpResponse(triage, status_code=200)
    return None
