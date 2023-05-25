from django.contrib import admin
from django.urls import path

from organizer import views as organizer_views


urlpatterns = [
    path('main/', organizer_views.MainPageView.as_view()),
    path('characters/', organizer_views.CharacterListView.as_view()),
]