from datacenter.models import Passcard
from django.shortcuts import render, get_list_or_404

def active_passcards_view(request):
    active_passcards = get_list_or_404(Passcard, is_active=True)
    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)




