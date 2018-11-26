from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.TipListView.as_view()),
    path('<int:pk>/', views.TipDetailView.as_view()),
]