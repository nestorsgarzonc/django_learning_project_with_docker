from django.http import HttpResponse, JsonResponse
from datetime import datetime


def hw(request):
    return HttpResponse(
        f'Server time: {datetime.now().strftime(r"%b %dth  %Y %H:%M")}'
    )


def hi(request, name: str):
    numbers = request.GET['numbers'].split(',')
    return JsonResponse({'numbers': sorted(numbers), 'name': name})
