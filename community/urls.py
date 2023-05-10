from django.urls import path
from . import views

urlpatterns = [
    path('', views.community, name='community'),
    path('category/<int:category_id>/',
         views.community_category, name='community_category'),
    path('posts/category/<int:category_id>/',
         views.community_category, name='posts_by_category'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/add_comment/',
         views.add_comment, name='add_comment'),
]
