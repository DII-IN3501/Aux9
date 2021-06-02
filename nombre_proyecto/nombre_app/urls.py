from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('formulario/', views.formulario, name="formulario"),
    path('resultados/', views.resultados, name="resultados"),
    path('login/', views.loginView, name = "login"),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logoutView, name='logout')
    ]
