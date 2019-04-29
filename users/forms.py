from django import forms
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """
    Class for registration form.
    """
    error_messages = {
        'password_mismatch': _("As duas senhas informadas não coincidem."),
    }
    first_name = forms.CharField(
        label=_("Nome"),
        help_text=_("Digite aqui o seu primeiro nome")
    )
    last_name = forms.CharField(
        label=_("Sobrenome"),
        help_text=_("Digite aqui o seu sobrenome")
    )
    username = forms.CharField(
        label=_("Nome de usuário"),
        help_text=_("Digite aqui um nome de usuário")
    )
    email = forms.CharField(
        label=_("E-mail"),
        help_text=_("Digite aqui o seu e-mail"),
        validators=[validate_email]
    )
    password = forms.CharField(
        label=_("Senha"),
        help_text=_("Digite aqui uma senha"),
        widget=forms.PasswordInput
    )
    password_validation = forms.CharField(
        label=_("Confirmar senha"),
        help_text=_("Digite aqui a senha escolhida novamente"),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")

    def clean_password_validation(self):
        password = self.cleaned_data.get("password")
        password_validation = self.cleaned_data.get("password_validation")
        if password and password_validation and password != password_validation:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password_validation

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
