from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': visitor.format_duration(),
        }
        for visitor in get_list_or_404(Visit, leaved_at__isnull=True)
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
