"""Defines URL patterns for climate."""

from django.urls import path

from . import views


app_name = 'climate'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path('on', views.desk_on, name='desk_on'),
    path('off', views.desk_off, name='desk_off'),
]

