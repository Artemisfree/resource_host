from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up),
    path('login/', views.log_in),
    path('/index/', views.host_page),
]
