from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('autenticacao/', include('users.urls')),
    path('paciente/', include('consultations.routes')),
    path('admin/', admin.site.urls),
]
