from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
