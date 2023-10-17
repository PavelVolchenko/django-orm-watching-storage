from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': visitor.format_duration(),
        }
        for visitor in Visit.objects.filter(leaved_at__isnull=True)
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

test_time = 60  # minutes
suspects = list()
passcode_list = Passcard.objects.values_list('passcode')
for passcode in passcode_list:
    print(f"{passcode=}")
    pk = Passcard.objects.filter(passcode=passcode)
    print(f"{pk=}")
    visit_list = Visit.objects.filter(passcard=pk).all()
    for visit in visit_list:
        print(visit)
        # if int(visit.get_duration()) >= test_time:
        #     suspects.append(passcode)

print(suspects)