from django.urls import path

from . import views

app_name = 'firstApp'
urlpatterns = [
    # ex: /firstApp
    path('', views.IndexView.as_view(), name='index'),
    ]
