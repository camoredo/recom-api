from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.LogoutView.as_view()),
]
