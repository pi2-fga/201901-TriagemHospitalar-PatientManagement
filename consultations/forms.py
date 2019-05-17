from django import forms
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from consultations.models import Patient


class PatientRegistrationForm(forms.ModelForm):
    """
    Class for Patient registration form.
    """
    error_messages = {
        'phone_error': _("Ao menos um número deve ser fornecido."),
    }
    first_name = forms.CharField(
        label=_("Nome"),
        help_text=_("Digite aqui o primeiro nome do paciente")
    )
    last_name = forms.CharField(
        label=_("Sobrenome"),
        help_text=_("Digite aqui o sobrenome do  paciente")
    )
    birthdate = forms.DateField(
        label=_("Data de Nascimento"),
        help_text=_("Data de nascimento do paciente"),
    )
    telefone_number = forms.CharField(
        label=_("Número de telefone"),
        help_text=_("Digite aqui o número de contato do paciente")
    )
    cellphone_number = forms.CharField(
        label=_("Número de celular"),
        help_text=_("Digite aqui o número de contato do paciente")
    )
    email = forms.CharField(
        label=_("E-mail"),
        help_text=_("Digite aqui o seu e-mail"),
        validators=[validate_email]
    )
    health_insurance = forms.CharField(
        label=_("Plano de Saúde"),
        help_text=_("Digite aqui o plano de saúde, caso seja apresentado"),
    )
    health_insurance_document = forms.ImageField(
        label=_("Documento do Plano de Saúde"),
        help_text=_("Cópia do plano de saúde, caso seja apresentado"),
    )

    class Meta:
        model = Patient
        fields = ("first_name", "last_name", "birthdate", "telefone_numbers",
                  "health_insurance", "health_insurance_document")

    def clean_phone_numbers(self):
        telefone_number = self.cleaned_data.get("telefone_number")
        cellphone_number = self.cleaned_data.get("cellphone_number")

        if not telefone_number and not cellphone_number:
            raise forms.ValidationError(
                self.error_messages['phone_error'],
                code='phone_error',
            )

        return {
            'fixo': telefone_number or None,
            'celular': cellphone_number or None,
        }

    def save(self, commit=True):
        patient = super(PatientRegistrationForm, self).save(commit=False)
        patient.set_telefone_numbers(self.clean_phone_numbers())
        if commit:
            patient.save()
        return patient
