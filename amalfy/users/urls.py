from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListCreateView.as_view()),
    path('login/', views.Login.as_view()),
    path('mood/', views.MoodCreateView.as_view()),
    path('<str:token>/', views.UserDetailView.as_view()),
    path('<str:token>/moods/', views.UserMoodListView.as_view())
]