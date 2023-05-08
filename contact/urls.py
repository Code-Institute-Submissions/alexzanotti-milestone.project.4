from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_management/', views.contact_management,
         name='contact_management'),
    path('contact_management/delete/<int:form_id>/',
         views.delete_contact_form, name='delete_contact_form'),
]
