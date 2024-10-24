from django.urls import path

from . import views


urlpatterns = [
   path('EmailServer/api', views.EmailServer, name='EmailServer')
]