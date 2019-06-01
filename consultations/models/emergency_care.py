import json
from django.db import models
from users.models import Medic
from consultations.models import Patient
from django.utils.translation import ugettext_lazy as _


class Triage(models.Model):
    """
    Class that represents the triage.

    Since the blood_pressure field is supposed
    to save a pair of values and the fields
    main_complaint, alergies, continuos_medication
    and previous_diagnosis are supposed to save
    a list of strings, those values will be
    serialized and stored as a JSON formatted
    string. Therefore, they should not be
    accessed directly.
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
    body_mass = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    blood_pressure = models.CharField(max_length=200)  # Pair of values
    blood_oxygen_level = models.FloatField()
    main_complaint = models.CharField(max_length=500, null=True, blank=True)  # List of values
    alergies = models.CharField(max_length=500)  # List of values
    continuos_medication = models.CharField(max_length=500)  # List of values
    previous_diagnosis = models.CharField(max_length=500)  # List of values
    height = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ticket_number = models.IntegerField()
    risk_level = models.IntegerField(
            choices=TRIAGE_RISK_CATEGORIES,
            default=RED,
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='triages',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Triage"
        verbose_name_plural = "Triages"

    def __str__(self):
        if self.patient is not None:
            response = self.patient.get_full_name() + "'s triage"
        else:
            response = "Patient not defined's triage"
        return response

    def set_blood_pressure(self, x):
        self.blood_pressure = json.dumps(x)

    def get_blood_pressure(self):
        return json.loads(self.blood_pressure)

    def set_main_complaint(self, x):
        self.main_complaint = json.dumps(x)

    def get_main_complaint(self):
        return json.loads(self.main_complaint)

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

    def get_blood_pressure_formatted(self):
        blood_pressure = self.get_blood_pressure()
        blood_pressure_formatted = "{}x{}".format(
            blood_pressure[0],
            blood_pressure[1]
        )
        return blood_pressure_formatted

class Consultation(models.Model):
    """
    class that represent an emergency consultation with a medic
    """
    medical_opinion = models.CharField(max_length=500)
    medic = models.ForeignKey(Medic, on_delete=models.PROTECT, null=True)
    triage = models.ForeignKey(
        Triage,
        on_delete=models.CASCADE,
        related_name='consultation',
        null=True
    )
    is_patient_released = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"

    def __str__(self):
        if self.triage is not None:
            response = self.triage.patient.get_full_name() + "'s consultation"
        else:
            response = "Patient not defined's consultation"
        return response
