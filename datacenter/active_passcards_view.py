from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def active_passcards_view(request):

    # active_visitors = Visit.objects.filter(leaved_at__isnull=True).all()
    # for visitor in active_visitors:
    #     print(f"\n        Сотрудник: {visitor.passcard.owner_name}")
    #     print(f"Зашёл в хранилище: {visitor.entered_at.strftime('%H:%M:%S (МСК) %d.%m.%Y')}")
    #     print(f" Время нахождения: {visitor.format_duration()}")

    active_passcards = Passcard.objects.filter(is_active=True).all()
    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)




