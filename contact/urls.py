from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_management/', views.contact_management,
         name='contact_management'),
]
