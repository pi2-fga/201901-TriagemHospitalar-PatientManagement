import json
from django.core.validators import validate_email
from django.db import models
from consultations.utils import validate_birthdate, validate_cpf
from datetime import date


class Patient(models.Model):
    """
    Class that represents the patient.

    Since the telephone_numbers field is supposed
    to save a list of strings, those values
    ​​will be serialized and stored as a JSON
    formatted string. Therefore, they should
    not be accessed directly.
    """

    GENDER_CHOICES = (
        (None, 'Null'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros')
    )

    first_name = models.CharField(max_length=200, default=None, null=True)
    last_name = models.CharField(max_length=200, default=None, null=True)
    birthdate = models.DateTimeField(validators=[validate_birthdate], default=None, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=None, null=True)
    id_document = models.ImageField(upload_to='static/images/', default=None, null=True)
    identification = models.CharField(max_length=200, validators=[validate_cpf], default=None, null=True)
    telefone_numbers = models.CharField(max_length=500, default=None, null=True)
    email = models.EmailField(max_length=200, default=None, null=True)
    health_insurance = models.CharField(max_length=200, blank=True, default=None, null=True)
    health_insurance_document = models.ImageField(upload_to='static/images/', blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

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

    def calculateAge(self):
        today = date.today()
        age = (today.year - self.birthdate.year -
               ((today.month, today.day) <
                (self.birthdate.month, self.birthdate.day)))
        return age

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def set_telefone_numbers(self, x):
        self.telefone_numbers = json.dumps(x)

    def get_telefone_numbers(self):
        return json.loads(self.telefone_numbers)
