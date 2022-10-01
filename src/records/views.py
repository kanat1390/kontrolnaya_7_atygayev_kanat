from django.shortcuts import render, redirect
from .services import record_services
from .forms import RecordModelForm
from django.http import HttpResponse

def record_list_view(request):
    form = RecordModelForm()
    record_list = record_services.get_records()
    context = {
        'record_list': record_list,
        'form': form,
    }
    return render(request, 'records/record_list.html', context)

def record_create_view(request):
    if request.method == "POST":
        form = RecordModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        return HttpResponse('"GET" request is not allowed')
    
def record_update_view(request, pk):
    record = record_services.get_record_by_pk(pk)
    form = RecordModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('record-list')
    context = {
        'form':form,
    }
    return render(request, 'records/record_update.html', context)

def record_delete_view(request, pk):
    record = record_services.get_record_by_pk(pk)
    context = {
        'record':record,
    }
    return render(request, 'records/record_delete.html', context)

def record_delete_confirm_view(request, pk):
    if request.method == "POST":
        record = record_services.get_record_by_pk(pk)
        record.delete()
        return redirect('record-list')
    return HttpResponse('"GET" request is not allowed')

