from django.urls import path

from shelves import views

app_name = 'shelves'

urlpatterns = [
    path('recommendations/',
         views.RecommendationListView.as_view(),
         name='recommend'),
    path('recommendations/<int:id>/', views.RecommendationView.as_view()),
]
