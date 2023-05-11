from django.urls import path, include
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name='community'),
    path('category/<int:category_id>/',
         views.community_category, name='community_category'),
    path('posts/category/<int:category_id>/',
         views.community_category, name='posts_by_category'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/add_comment/',
         views.add_comment, name='add_comment'),
    path('add_post/', views.add_post, name='add_post'),
    path('community_management/', views.community_management,
         name='community_management'),
    path('community_management/add_category/',
         views.add_category, name='add_category'),
    path('community_management/edit_category/<int:category_id>/',
         views.edit_category, name='edit_category'),
    path('community_management/delete_category/<int:category_id>/',
         views.delete_category, name='delete_category'),
    path('community_management/edit_post/<int:post_id>/',
         views.edit_post, name='edit_post'),
    path('community_management/delete_post/<int:post_id>/',
         views.delete_post, name='delete_post'),
    path('community_management/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('community_management/edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
]
