from django.shortcuts import render, redirect
from boogie.router import Router
from consultations.models.emergency_care import Triage


urlpatterns = Router()


@urlpatterns.route()
def index(request):
    """
    [...]
    """

    if request.user.is_authenticated:

        if hasattr(request.user, 'medic'):
            response = redirect('/medic')
        elif hasattr(request.user, 'clerk'):

            triage_queue = Triage.objects.filter(
                patient=None
            ).order_by(
                'risk_level',
                'created_at'
            )

            try:
                next_patient = triage_queue.first().id
            except AttributeError:
                next_patient = None

            triage_queue_list = list()

            for index, triage in enumerate(triage_queue):

                triage_information = dict()
                triage_information['position'] = index+1
                triage_information['name'] = triage.name
                triage_information['age'] = triage.age
                triage_information['date_hour'] = triage.created_at
                triage_information['risk'] = dict()
                triage_information['risk']['background_color'] = \
                    Triage.TRIAGE_RISK_CATEGORIES[triage.risk_level][1]

                if triage.risk_level == 0:
                    triage_information['risk']['text'] = 'VERMELHO'
                    triage_information['risk']['text_color'] = 'white'
                elif triage.risk_level == 1:
                    triage_information['risk']['text'] = 'AMARELO'
                    triage_information['risk']['text_color'] = 'black'

                elif triage.risk_level == 2:
                    triage_information['risk']['text'] = 'VERDE'
                    triage_information['risk']['text_color'] = 'white'
                elif triage.risk_level == 3:
                    triage_information['risk']['text'] = 'AZUL'
                    triage_information['risk']['text_color'] = 'white'

                triage_queue_list.append(triage_information)

            response = render(
                request,
                'clerk_homepage.html',
                {
                    'next_patient': next_patient,
                    'triage_queue_list': triage_queue_list
                }
            )
        elif request.user.is_superuser:
            response = redirect('/super_user')

    else:

        response = render(request, 'homepage.html')

    return response
