from django import forms
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from consultations.models import Patient, Consultation


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
        help_text=_("Digite aqui o primeiro nome do paciente")
    )
    last_name = forms.CharField(
        label=_("Sobrenome"),
        help_text=_("Digite aqui o sobrenome do paciente")
    )
    birthdate = forms.DateField(
        label=_("Data de Nascimento"),
        help_text=_("Data de nascimento do paciente")
    )
    telefone_number = forms.CharField(
        label=_("Número de telefone"),
        help_text=_("Digite aqui o número de contato do paciente")
    )
    cellphone_number = forms.CharField(
        label=_("Número de celular"),
        help_text=_("Digite aqui o número de contato do paciente")
    )
    email = forms.EmailField(
        label=_("E-mail"),
        help_text=_("Digite aqui o e-mail do paciente")
    )
    health_insurance = forms.CharField(
        label=_("Plano de Saúde"),
        help_text=_("Digite aqui o plano de saúde, caso seja apresentado")
    )
    health_insurance_document = forms.ImageField(
        label=_("Documento do Plano de Saúde"),
        help_text=_("Cópia do plano de saúde, caso seja apresentado"),
        required=False
    )
    id_document = forms.ImageField(
        label=_("Documento do identificação"),
        help_text=_(
            "Neste campo você deve enviar: identidade, CNH, ou " +
            "algum documento ofical com foto que possa identificá-lo."
        ),
        required=False
    )
    identification = forms.CharField(
        label=_("CPF"),
        help_text=_("Digite aqui o CPF do paciente")
    )
    gender = forms.CharField(
        label=_("Gênero"),
        help_text=_("Marque aqui o gênero do paciente")
    )

    class Meta:
        model = Patient
        fields = (
            "first_name", "last_name", "birthdate", "gender", "id_document",
            "health_insurance", "health_insurance_document", "identification"
        )

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


TRUE_FALSE_CHOICES = (
    (True, 'Sim'),
    (False, 'Não')
)


class ConsultationForm(forms.ModelForm):

    medical_opinion = forms.CharField(
        label=_("Opinião médica"),
        help_text=_("Digite aqui a sua opinião sobre o caso do paciente")
        # widget=forms.Textarea(attrs={'placeholder':_("Digite")})
    )
    is_patient_released = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES,
        label="Liberar paciente?",
        initial='',
        widget=forms.RadioSelect
    )

    class Meta:
        model = Consultation
        fields = ("medical_opinion", "is_patient_released")
