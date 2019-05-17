import datetime
from django.core.exceptions import ValidationError


def validate_birthdate(value):
    now = datetime.datetime.now()

    if value.year < 1900 or value > now:
        raise ValidationError('%s não é uma data válida' % value)
