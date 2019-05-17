from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from consultations.forms import PatientRegistrationForm


class PatientRegistrationView(FormView):
    template_name = 'patient_registration.html'
    form_class = PatientRegistrationForm
    success_url = '/'

    def post(self, request):
        form = PatientRegistrationForm(request.POST)

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
