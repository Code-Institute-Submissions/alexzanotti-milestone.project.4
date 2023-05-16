from django.urls import path
from . import views


app_name = 'plans'


urlpatterns = [
    path('', views.plans, name='plans'),
    path('plan_management/', views.plan_management, name='plan_management'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/',
         views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/',
         views.delete_category, name='delete_category'),
    path('add_plan/', views.add_plan, name='add_plan'),
    path('edit_plan/<int:plan_id>/', views.edit_plan, name='edit_plan'),
    path('delete_plan/<int:plan_id>/', views.delete_plan, name='delete_plan'),
    path('my_plans/', views.my_plans, name='my_plans'),
    path('<int:plan_id>/', views.plan_description, name='plan_description'),
    path('add_comment/<int:plan_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
]
