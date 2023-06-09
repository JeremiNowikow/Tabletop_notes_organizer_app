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
    path('locations/', organizer_views.LocationListView.as_view(), name='locations'),
    path('locations/delete/<int:id>/', organizer_views.DeleteLocation.as_view(), name='delete-location'),
    path('locations/<int:id>/', organizer_views.ShowLocationDetails.as_view(), name='location-details'),
    path('characters/add-relationship/<int:id>/', organizer_views.AddRelationship.as_view(), name='add-relationship'),
    path('relationships/delete/<int:id>/<int:char_id>/', organizer_views.DeleteRelationship.as_view(), name='delete-relationship'),
    path('relationships/edit/<int:id>/<int:char_id>/', organizer_views.EditRelationship.as_view(), name='edit-relationship'),
    path('relationships/<int:id>/<int:char_id>/', organizer_views.RelationshipDetails.as_view(), name='relationship-details'),
    path('add-location/', organizer_views.AddLocation.as_view(), name='add-location'),
    path('locations/edit/<int:id>/', organizer_views.EditLocation.as_view(), name='edit-location'),
    path('lore-events/', organizer_views.LoreEventListView.as_view(), name='lore-events'),
    path('lore-events/<int:id>/', organizer_views.LoreEventDetails.as_view(), name='lore-event-details'),
    path('lore-events/delete/<int:id>/', organizer_views.DeleteLoreEvent.as_view(), name='delete-lore-event'),
    path('lore-events/edit/<int:id>/', organizer_views.EditLoreEvent.as_view(), name='edit-lore-event'),
    path('add-lore-event/', organizer_views.AddLoreEvent.as_view(), name='add-lore-event'),
    path('campaign-events/', organizer_views.CampaignEventListView.as_view(), name='campaign-events'),
    path('campaign-events/delete/<int:id>/', organizer_views.DeleteCampaignEvent.as_view(), name='delete-campaign-event'),
    path('campaign-events/<int:id>/', organizer_views.CampaignEventDetails.as_view(), name='campaign-event-details'),
    path('campaign-events/add-above/<int:id>/', organizer_views.AddCampaignEventAbove.as_view(), name='add-campaign-event-above'),
    path('campaign-events/add/', organizer_views.AddCampaignEventEnd.as_view(), name='add-campaign-event-end'),
    path('campaign-events/edit/<int:id>/', organizer_views.EditCampaignEvent.as_view(), name='edit-campaign-event'),





]