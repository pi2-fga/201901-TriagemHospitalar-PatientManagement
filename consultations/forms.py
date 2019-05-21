from django import forms
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from consultations.models import Patient

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientRegistrationForm(forms.ModelForm):
    """
    Class for Patient registration form.
    """
    error_messages = {
        'phone_error': _("Ao menos um número deve ser fornecido."),
    }
    first_name = forms.CharField(
        label=_("Nome"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui o primeiro nome do paciente")})
    )
    last_name = forms.CharField(
        label=_("Sobrenome"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui o sobrenome do  paciente")})
    )
    birthdate = forms.DateField(
        label=_("Data de Nascimento"),
        widget=DateInput(attrs={'placeholder':_("Data de nascimento do paciente")})
    )
    telefone_number = forms.CharField(
        label=_("Número de telefone"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui o número de contato do paciente")})
    )
    cellphone_number = forms.CharField(
        label=_("Número de celular"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui o número de contato do paciente")})
    )
    email = forms.CharField(
        label=_("E-mail"),
        widget=forms.EmailInput(attrs={'placeholder':_("Digite aqui o seu e-mail")}),
        validators=[validate_email]
    )
    health_insurance = forms.CharField(
        label=_("Plano de Saúde"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui o plano de saúde, caso seja apresentado")}),
    )
    health_insurance_document = forms.ImageField(
        label=_("Documento do Plano de Saúde"),
        widget=forms.FileInput(attrs={'placeholder':_("Cópia do plano de saúde, caso seja apresentado")}),
    )
    id_document = forms.ImageField(
        label=_("Documento do identificação"),
        widget=forms.FileInput(attrs={'placeholder':_("Neste campo você deve enviar: identidade, CNH, ou algum documento ofical com foto que possa identificá-lo. ")}),
    )
    identification = forms.CharField(
        label=_("CPF"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui seu cpf")}),
    )

    gender = forms.CharField(
        label=_("Gênero"),
        widget=forms.TextInput(attrs={'placeholder':_("Digite aqui seu genero")}),
    )
    class Meta:
        model = Patient
        fields = ("first_name", "last_name", "birthdate", 
                  "health_insurance", "health_insurance_document", "identification")

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
