from django.urls import path
from . import views

urlpatterns = [
    path('', views.community, name='community'),
    path('posts/category/<int:category_id>/',
         views.community_category, name='community_category'),
]
