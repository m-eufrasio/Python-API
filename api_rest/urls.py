from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_users, name='get_all_users'),
  path('user/<str:nick>', views.get_by_nick),
  path('data/', views.user_manager) # A barra no final do data não é obrigatório
]