from django.urls import path
from .views import (
    record_list_view,
    record_update_view,
    record_delete_view,
    record_delete_confirm_view,
    record_create_view,
)
urlpatterns=[
    path('', record_list_view, name='record-list'),
    path('records/create/', record_create_view, name='record-create'),
    path('records/<int:pk>/update/', record_update_view, name='record-update'),
    path('records/<int:pk>/delete/', record_delete_view, name='record-delete'),
    path('records/<int:pk>/delete/confirm', record_delete_confirm_view, name="record-delete-confirm"),
]