from django.contrib import admin
from .models import Patient, Triage, Consultation

# Register your models here.
admin.site.register(Patient)
admin.site.register(Triage)
admin.site.register(Consultation)
