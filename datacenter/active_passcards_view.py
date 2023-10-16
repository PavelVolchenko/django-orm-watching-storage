from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    # [print(note) for note in Visit.objects.all()]
    [print(note) for note in Visit.objects.filter(leaved_at__isnull=True).all()]

    active_passcards = Passcard.objects.filter(is_active=True).all()
    context = {
        'active_passcards': active_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)




