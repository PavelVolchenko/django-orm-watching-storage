from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import datetime

def active_passcards_view(request):
    # Программируем здесь

    active_visitors = Visit.objects.filter(leaved_at__isnull=True).all()
    for visitor in active_visitors:
        delta = localtime() - visitor.entered_at
        delta = datetime.timedelta(seconds=int(delta.total_seconds()))
        print(f"\nЗашёл в хранилище, время по Москве:\n{visitor.entered_at}")
        print(f"Находится в хранилище:\n{delta}")


    active_passcards = Passcard.objects.filter(is_active=True).all()
    context = {
        'active_passcards': active_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)




