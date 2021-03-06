from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.routes')),
    path('autenticacao/', include('users.routes')),
    path('paciente/', include('consultations.routes')),
    path('admin/', admin.site.urls),
]
