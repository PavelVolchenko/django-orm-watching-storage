from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404, get_list_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(),
            'is_strange': visit.is_visit_long(),
        } for visit in get_list_or_404(Visit, passcard=passcard)
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
