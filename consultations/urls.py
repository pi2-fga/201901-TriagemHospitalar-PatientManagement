from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/', views.PatientRegistrationView.as_view(),
         name='patient_sign_up'),
    
]
