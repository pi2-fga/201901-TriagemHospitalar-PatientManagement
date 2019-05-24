from django.shortcuts import render, redirect
from boogie.router import Router
from consultations import models
from consultations.forms import PatientRegistrationForm, ConsultationForm
from consultations.models import Triage

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
    form = ConsultationForm
    return render(request, 'patient_detail.html',
                  {'form': form, 'patient': patient_triage.patient,
                   'triage': patient_triage.triage})


@urlpatterns.route('cadastrar/' + triage_url)
def patient_registration(request, triage):
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
