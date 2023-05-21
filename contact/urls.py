from django.urls import path
from . import views

urlpatterns = [
     path('', views.contact, name='contact'),
     path('contact_management/', views.contact_management,
         name='contact_management'),
     path('contact_management/update/<int:contact_id>/',
         views.update_contact_form, name='update_contact_form'),
     path('contact_management/delete/<int:form_id>/',
         views.delete_contact_form, name='delete_contact_form'),
     path('contact_success/', views.contact_success, name='contact_success'),
]
