from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from consultations.forms import PacientRegistrationForm


class PacientRegistrationView(FormView):
    template_name = 'pacient_registration.html'
    form_class = PacientRegistrationForm
    success_url = '/'

    def post(self, request):

        form = PacientRegistrationForm(request.POST)

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
