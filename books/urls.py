from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('search/', views.SearchView.as_view()),
]
