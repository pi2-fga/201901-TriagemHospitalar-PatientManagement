from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/', views.PacientRegistrationView.as_view(),
         name='patient_sign_up'),
]
