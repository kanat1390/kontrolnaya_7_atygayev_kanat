from ..models import Record
from django.shortcuts import get_object_or_404
def get_records():
    return Record.objects.active()

def get_record_by_pk(pk):
    return get_object_or_404(Record, pk=pk)
