from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.article_list, name='list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('', views.home, name='home')
]
