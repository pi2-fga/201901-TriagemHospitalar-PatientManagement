import json
from django.db import models
from users.models import Medic
from consultations.models import Patient
from django.utils.translation import ugettext_lazy as _


class Triage(models.Model):
    """
    Class that represents the triage.

    Since the blood_pressure field is supposed
    to save a pair of values and the fields alergies,
    continuos_medication and previous_diagnosis
    are supposed to save a list of strings,
    those values ​​will be serialized and stored
    as a JSON formatted string. Therefore,
    they should not be accessed directly.
    """
    RED = 0
    YELLOW = 1
    GREEN = 2
    BLUE = 3
    TRIAGE_RISK_CATEGORIES = [
        (RED, _('red')),
        (YELLOW, _('yellow')),
        (GREEN, _('green')),
        (BLUE, _('blue')),
    ]
    body_temperature = models.FloatField()
    body_mass = models.FloatField()
    blood_pressure = models.CharField(max_length=200)  # Pair of values
    blood_oxygen_level = models.FloatField()
    main_complaint = models.CharField(max_length=500, null=True, blank=True)
    alergies = models.CharField(max_length=500)  # List of values
    continuos_medication = models.CharField(max_length=500)  # List of values
    previous_diagnosis = models.CharField(max_length=500)  # List of values
    height = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ticket_number = models.IntegerField()
    risk_level = models.IntegerField(
            choices=TRIAGE_RISK_CATEGORIES,
            default=RED,
    )

    def set_blood_pressure(self, x):
        self.blood_pressure = json.dumps(x)

    def get_blood_pressure(self):
        return json.loads(self.blood_pressure)

    def set_alergies(self, x):
        self.alergies = json.dumps(x)

    def get_alergies(self):
        return json.loads(self.alergies)

    def set_continuos_medication(self, x):
        self.continuos_medication = json.dumps(x)

    def get_continuos_medication(self):
        return json.loads(self.continuos_medication)

    def set_previous_diagnosis(self, x):
        self.previous_diagnosis = json.dumps(x)

    def get_previous_diagnosis(self):
        return json.loads(self.previous_diagnosis)


class PatientTriage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    triage = models.ForeignKey(Triage, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Consultation(models.Model):
    """
    class that represent an emergency consultation with a medic
    """
    medical_opinion = models.CharField(max_length=500)
    medic = models.ForeignKey(Medic, on_delete=models.PROTECT, null=True)
    patient_triage = models.ForeignKey(PatientTriage, on_delete=models.CASCADE,
                                       null=True)
    is_patient_released = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
