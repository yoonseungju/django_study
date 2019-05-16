from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.Index, name='index'),
]