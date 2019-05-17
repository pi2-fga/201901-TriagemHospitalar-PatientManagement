import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_birthdate(value):
    now = datetime.datetime.now()

    if value.year < 1900 or value > now:
        raise ValidationError(_('%s não é uma data válida' % value))
