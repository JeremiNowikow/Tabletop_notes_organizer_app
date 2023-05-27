from django.contrib import admin
from django.urls import path

from organizer import views as organizer_views


urlpatterns = [
    path('', organizer_views.MainPageView.as_view(), name='main'),
    path('characters/', organizer_views.CharacterListView.as_view(), name='characters'),
    path('characters/<int:id>/', organizer_views.ShowCharacterDetails.as_view(), name='character-details'),
    path('characters/delete/<int:id>/', organizer_views.DeleteCharacter.as_view(), name='delete-character'),
    path('add-player-character/', organizer_views.AddPlayerCharacter.as_view(), name='add-player'),
    path('add-nonplayable-character/', organizer_views.AddNonPlayableCharacter.as_view(), name='add-npc'),
    path('characters/edit/<int:id>/', organizer_views.EditCharacter.as_view(), name='edit-character'),

]