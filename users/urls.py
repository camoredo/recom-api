from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UserList.as_view()),
    path('register/', views.RegistrationView.as_view(), name='register'),
]
