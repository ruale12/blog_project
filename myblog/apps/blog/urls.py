from django.urls import path
from . import views;

urlpatterns = [
    path('home/', views.index, name = "home"),
    path('categorias/', views.category, name = "categorias"),
]
