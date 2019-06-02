from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from boogie.router import Router
from consultations.models.emergency_care import Triage, Call


urlpatterns = Router()


@urlpatterns.route()
def index(request):
    """
    [...]
    """

    if request.user.is_authenticated:

        if hasattr(request.user, 'medic'):

            response = redirect('/chamada-de-pacientes/')

        elif hasattr(request.user, 'clerk'):

            response = redirect('/registro-de-pacientes/')

        elif request.user.is_superuser:

            response = render(request, 'homepage.html')

    else:

        response = render(request, 'homepage.html')

    return response


@urlpatterns.route('registro-de-pacientes/')
def patient_register(request):
    """
    [...]
    """

    if hasattr(request.user, 'clerk') or request.user.is_superuser:

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

    else:

        response = redirect('/')

    return response


@urlpatterns.route('chamada-de-pacientes/')
def patient_call(request):
    """
    [...]
    """

    if hasattr(request.user, 'medic') or request.user.is_superuser:

        triage_queue = Triage.objects.filter(
            ~Q(patient=None),
            consultation=None
        ).order_by(
            'risk_level',
            'created_at'
        )

        try:
            next_patient = triage_queue.first().patient.id
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
            'medic_homepage.html',
            {
                'next_patient': next_patient,
                'triage_queue_list': triage_queue_list
            }
        )

    else:

        response = redirect('/')

    return response


@urlpatterns.route('chamadas/')
def patient_calls(request):
    """
    [...]
    """

    response = render(
        request,
        'calls.html'
    )

    return response


@urlpatterns.route('chamadas/checar-mudancas/')
def patient_calls_checker(request):
    """
    [...]
    """

    calls = Call.objects.filter().order_by(
        '-created_at'
    )[:5]

    response = dict()
    response['calls'] = list()

    for call in calls:

        call_dict = dict()

        if call.medic is not None:
            call_dict['caller'] = call.medic.get_full_name()
            call_dict['patient'] = call.patient.get_full_name()
            call_dict['type'] = 'CONSULTA'
        elif call.clerk is not None:
            call_dict['caller'] = call.clerk.get_full_name()
            call_dict['patient'] = call.patient_name
            call_dict['type'] = 'CADASTRAMENTO'

        call_dict['location'] = call.location
        call_dict['time'] = call.created_at

        response['calls'].append(call_dict)

    if calls.count() < 5:

        for i in range(5-calls.count()):

            call_dict = dict()
            call_dict['caller'] = None
            call_dict['patient'] = None
            call_dict['type'] = None
            call_dict['location'] = None
            call_dict['time'] = None

            response['calls'].append(call_dict)

    return JsonResponse(response)
