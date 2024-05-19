from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_list, name='notes_list'),
    path("notes_list/", views.notes_list, name='notes_list'),
    path('add_note/', views.add_note, name='add_note'),
    path("detail_note/<int:id>/", views.detail_note, name='detail_note'),
    path("edit_note/<int:id>/", views.edit_note, name='edit_note'),
]