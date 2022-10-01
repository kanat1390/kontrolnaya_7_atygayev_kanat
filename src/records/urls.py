from django.urls import path
from .views import (
    record_list_view,
)
urlpatterns=[
    path('', record_list_view, name='record-list'),
]