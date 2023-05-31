from django.contrib import admin
from django.urls import path

from account import views as acc_views

urlpatterns = [
    path('login/', acc_views.LoginView.as_view(), name='login'),
    path('logout/', acc_views.LogoutView.as_view(), name='logout'),
    path('sign_up/', acc_views.CreateUserViews.as_view(), name='sign_up'),
]
