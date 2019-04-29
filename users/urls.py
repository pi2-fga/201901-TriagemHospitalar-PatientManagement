from django.urls import path

from . import views

urlpatterns = [
    path('criar-conta/', views.RegistrationView.as_view(), name='sign_up'),
    path('efetuar-login/', views.sign_in, name='sign_in'),
]
