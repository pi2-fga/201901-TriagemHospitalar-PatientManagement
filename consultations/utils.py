import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from pycpfcnpj import cpfcnpj
import pytz


def validate_birthdate(value):
    now = datetime.datetime.now()
    utc = pytz.UTC
    now = utc.localize(now)
    if value.year < 1900 or value > now:
        raise ValidationError(_('%s não é uma data válida' % value))


def validate_cpf(value):
    if not cpfcnpj.validate(value):
        raise ValidationError(_('%s não é um cpf válido' % value))
