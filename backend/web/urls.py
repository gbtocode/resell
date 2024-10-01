from django.urls import path, include

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
]