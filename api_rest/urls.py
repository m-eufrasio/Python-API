from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
  path('', views.get_users, name='get_all_users'),
  path('user/<str:nick>', views.get_by_nick),
  path('data/', views.user_manager), # A barra no final do data não é obrigatório
  
  path('token/', MyTokenObtainPairView.as_view(), name='my_token_obtain_pair_view'),
  path('token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
]