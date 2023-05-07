from django.urls import path
from . import views

urlpatterns = [
    path('<int:plan_id>/', views.checkout, name='checkout'),
]
