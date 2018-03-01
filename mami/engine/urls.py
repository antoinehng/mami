from django.urls import path

from .webgui import views_manage as manage

urlpatterns = [
    path('', manage.dashboard, name='dashboard'),
]