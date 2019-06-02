from django.contrib import admin
from .models import Patient, Triage, Consultation, Call

admin.site.register(Patient)
admin.site.register(Triage)
admin.site.register(Consultation)
admin.site.register(Call)
