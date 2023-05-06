from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<plan_id>/', views.plan_sales_page, name='plan_sales_page'),
]
