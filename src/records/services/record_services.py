from ..models import Record

def get_records():
    return Record.objects.active()