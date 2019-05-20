from django.urls import path

from . import views

urlpatterns = [
    path('efetuar-login/', views.sign_in, name='sign_in'),
]
