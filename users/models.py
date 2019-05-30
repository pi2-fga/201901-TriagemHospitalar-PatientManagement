from django.db import models
from django.contrib.auth.models import User


class Medic(User):
    """
    Class that represents the medic.
    """
    crm = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Medic"
        verbose_name_plural = "Medics"

    def __str__(self):
        return self.get_full_name()

    def call_pacient_for_consultation(self):
        pass


class Clerk(User):
    """
    Class that represents the clerk.
    """

    class Meta:
        verbose_name = "Clerk"
        verbose_name_plural = "Clerks"

    def __str__(self):
        return self.get_full_name()

    def call_pacient_for_registration(self):
        pass
