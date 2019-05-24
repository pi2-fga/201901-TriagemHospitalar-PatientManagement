from django.shortcuts import render
from boogie.router import Router
from consultations import models
from consultations.forms import ConsultationForm


app_name = 'consultations'
urlpatterns = Router(
    models={
        'patient': models.Patient,
    },
    lookup_field={
        'patient': 'pk',
    },
)
patient_url = f'<model:patient>/'


# Must import after urlpatterns
@urlpatterns.route(patient_url)
def detail(request, patient):
    form = ConsultationForm
    return render(request, 'patient_detail.html',
                  {'form': form, 'patient': patient})
