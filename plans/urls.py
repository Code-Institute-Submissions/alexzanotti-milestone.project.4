from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('plan_management/', views.plan_management, name='plan_management'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/',
         views.edit_category, name='edit_category'),
    path('<plan_id>/', views.plan_sales_page, name='plan_sales_page'),
]
