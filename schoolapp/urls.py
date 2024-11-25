from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPageView, name='login'),
]
