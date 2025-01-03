from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.getRoutes),
    path('posts/', views.getPosts),
    path('posts/<str:pk>/', views.getPost),
]


urlpatterns = format_suffix_patterns(urlpatterns)