from django.urls import path, include

from . import views

urlpatterns = [
    path('cadastrar/', views.PatientRegistrationView.as_view(),
         name='patient_sign_up'),
    path('consulta/', include('consultations.routes')),

]
