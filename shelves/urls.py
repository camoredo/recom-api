from django.urls import path

from shelves import views

app_name = 'shelves'

urlpatterns = [
    path('recommendations/', views.RecommendView.as_view(), name='recommend'),
]
