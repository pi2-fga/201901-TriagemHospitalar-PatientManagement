from django.contrib import admin
from .models import Patient, Triage, Consultation

admin.site.register(Patient)
admin.site.register(Triage)
admin.site.register(Consultation)
