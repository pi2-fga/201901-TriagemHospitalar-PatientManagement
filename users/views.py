from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'sign_up.html'
    form_class = RegistrationForm
    success_url = '/'

    def post(self, request):

        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            response = redirect(self.success_url)
        else:
            response = render(request, self.template_name, {'form': form})

        return response

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


def sign_in(request):
    return render(request, 'sign_in.html')
