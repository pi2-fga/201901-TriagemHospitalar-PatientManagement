from django.db import models

import json


class Patient(models.Model):
    """
    Class that represents the patient.

    Since the telephone_numbers field is supposed
    to save a list of strings, those values
    ​​will be serialized and stored as a JSON
    formatted string. Therefore, they should
    not be accessed directly.
    """

    first_name = models.CharField()
    last_name = models.CharField()
    birthday = models.DateTimeField()
    gender = models.CharField()
    id_document = models.ImageField()
    identification = models.CharField()
    telefone_numbers = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '{firt_name} {last_name}'.format(
            firt_name=self.first_name,
            last_name=self.last_name
        )
        return full_name.strip()
    
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def set_telefone_numbers(self, x):
        self.telefone_numbers = json.dumps(x)

    def get_telefone_numbers(self):
        return json.loads(self.telefone_numbers)


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

    body_temperature = models.FloatField()
    body_mass = models.FloatField()
    blood_glucose = models.IntegerField()
    blood_pressure = models.CharField()  # Pair of values
    blood_oxygen_level = models.FloatField()
    alergies = models.CharField()  # List of values
    continuos_medication = models.CharField()  # List of values
    previous_diagnosis =  models.CharField()  # List of values
    height = models.FloatField()
    health_insurance = models.CharField()
    health_insurance_document = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
