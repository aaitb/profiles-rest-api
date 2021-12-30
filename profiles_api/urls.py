from django.urls import path

from profiles_api import views


urlpatterns = [
    path('hello-view/', views.TestApiView.as_view()),
]
