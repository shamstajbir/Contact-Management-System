from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  # View to display list of contacts
    path('add/', views.add_contact, name='add_contact'),  # View to add a new contact
    path('<int:id>/', views.contact_detail, name='contact_detail'),  # View to display details of a specific contact
    path('<int:id>/edit/', views.edit_contact, name='edit_contact'),  # View to edit a specific contact
    path('<int:id>/delete/', views.delete_contact, name='delete_contact'),  # View to delete a specific contact
]
