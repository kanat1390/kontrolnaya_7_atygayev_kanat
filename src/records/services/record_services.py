from ..models import Record
from django.shortcuts import get_object_or_404
def get_records():
    return Record.objects.active()

def get_record_by_pk(pk):
    return get_object_or_404(Record, pk=pk)

def search_records_by_author(author_name):
    print(Record.objects.active().filter(author__icontains=author_name))
    return Record.objects.active().filter(author__icontains=author_name)
