from django.urls import path
from . import views


app_name = 'checkout'


urlpatterns = [
    path('<int:plan_id>/', views.checkout, name='checkout'),
]
