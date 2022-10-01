from django.shortcuts import render
from .services import record_services

def record_list_view(request):
    record_list = record_services.get_records()
    context = {
        'record_list': record_list,
    }
    return render(request, 'records/record_list.html', context)