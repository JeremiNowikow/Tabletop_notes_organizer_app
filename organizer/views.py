import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView
from organizer.additional_functions import validate_age_or_level
from organizer.models import *
from django.db.models import Q


# Create your views here.


# shows starting page of the app
class MainPageView(View):
    def get(self, request):
        return render(request, 'organizer/main_page.html')


# shows a list of all character in the database with their name and short summary of their purpose
class CharacterListView(View):
    def get(self, request):
        characters = Character.objects.all().order_by('name')
        paginator = Paginator(characters, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/characters.html', {'page_obj': page_obj})

    def post(self, request):
        if 'all-chars' in request.POST:
            characters = Character.objects.all().order_by('name')
        elif 'only-pcs' in request.POST:
            characters = PlayerCharacter.objects.all().order_by('name')
        elif 'only-npcs' in request.POST:
            characters = NonPlayableCharacter.objects.all().order_by('name')
        elif 'search' in request.POST:
            search = request.POST.get('searchText')
            characters = Character.objects.filter(name__icontains=search).order_by('name')
        paginator = Paginator(characters, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/characters.html', {'page_obj': page_obj})


# shows all information about the chosen character
class ShowCharacterDetails(View):
    def get(self, request, id):
        character = Character.objects.get(pk=id)
        if isinstance(character, PlayerCharacter):
            player_char = True
        else:
            player_char = False

        relationships = character.relationships.through.objects.filter(Q(first_person=character.pk) | Q(second_person=character.pk))

        return render(request, 'organizer/character_view.html', {'player_char': player_char, 'character': character, 'relationships': relationships})


# deletes the chosen character from the database
class DeleteCharacter(View):
    def get(self, request, id):
        character = Character.objects.get(pk=id)
        character.delete()
        return redirect('characters')


# adds a new player character through a form
class AddPlayerCharacter(View):
    def get(self, request):
        return render(request, 'organizer/create_character.html', {'player': True})
    def post(self, request):

        name = request.POST.get('name')
        short_description = request.POST.get('short_description')
        gender = request.POST.get('gender')
        race = request.POST.get('race')
        age = request.POST.get('age')
        appearance = request.POST.get('appearance')
        backstory = request.POST.get('backstory')
        gm_notes = request.POST.get('gm_notes')
        player = request.POST.get('player')
        character_class = request.POST.get('character_class')
        level = request.POST.get('level')
        character_sheet = request.POST.get('character_sheet')

        age = validate_age_or_level(age)
        level = validate_age_or_level(level)


        PlayerCharacter.objects.create(
            name=name,
            short_description=short_description,
            gender=gender,
            race=race,
            age=age,
            appearance_description=appearance,
            backstory=backstory,
            gm_notes=gm_notes,
            player=player,
            character_class=character_class,
            level=level,
            character_sheet=character_sheet,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()

        )
        return redirect('characters')


# adds a new non-playable character through a form
class AddNonPlayableCharacter(View):
    def get(self, request):
        return render(request, 'organizer/create_character.html', {'player': False})
    def post(self, request):
        name = request.POST.get('name')
        short_description = request.POST.get('short_description')
        gender = request.POST.get('gender')
        race = request.POST.get('race')
        age = request.POST.get('age')
        appearance = request.POST.get('appearance')
        backstory = request.POST.get('backstory')
        gm_notes = request.POST.get('gm_notes')
        role = request.POST.get('role')
        history_with_players = request.POST.get('history_with_players')
        stat_block = request.POST.get('stat_block')

        age = validate_age_or_level(age)

        NonPlayableCharacter.objects.create(
            name=name,
            short_description=short_description,
            gender=gender,
            race=race,
            age=age,
            appearance_description=appearance,
            backstory=backstory,
            gm_notes=gm_notes,
            role=role,
            history_with_players=history_with_players,
            stat_block=stat_block,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()

        )
        return redirect('characters')


# edits information about an existing character
class EditCharacter(View):
    def get(self, request, id):
        character = Character.objects.get(pk=id)
        if isinstance(character, PlayerCharacter):
            player = True
        else:
            player = False
        return render(request, 'organizer/edit_character.html', {'character': character, 'player': player})
    def post(self, request, id):
        character = Character.objects.get(pk=id)

        character.name = request.POST.get('name')
        character.short_description = request.POST.get('short_description')
        character.gender = request.POST.get('gender')
        character.race = request.POST.get('race')
        age = request.POST.get('age')
        character.appearance_description = request.POST.get('appearance')
        character.backstory = request.POST.get('backstory')
        character.gm_notes = request.POST.get('gm_notes')
        character.updated_at = datetime.datetime.now()

        character.age = validate_age_or_level(age)

        if isinstance(character, PlayerCharacter):
            character.player = request.POST.get('player')
            character.character_class = request.POST.get('character_class')
            level = request.POST.get('level')
            character.level = validate_age_or_level(level)
        else:
            character.role = request.POST.get('role')
            character.history_with_players = request.POST.get('history_with_players')
        character.save()
        return redirect('character-details', id=character.pk)


# displays the list of all location in the database
class LocationListView(View):
    def get(self, request):
        locations = Location.objects.all().order_by('name')
        paginator = Paginator(locations, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/locations.html', {'page_obj': page_obj})

    def post(self, request):
        if 'search' in request.POST:
            search = request.POST.get('searchText')
            locations = Location.objects.filter(name__icontains=search).order_by('name')
        paginator = Paginator(locations, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/locations.html', {'page_obj': page_obj})


# creates a new relationship between two characters
class AddRelationship(View):
     def get(self, request, id):
          character = Character.objects.get(pk=id)
          all_characters = Character.objects.filter(~Q(pk=id))
          return render(request, 'organizer/create_relationship.html', {'character': character, 'all_characters': all_characters})
     def post(self, request, id):
          first_character = Character.objects.get(pk=id)
          second_character = Character.objects.get(pk=request.POST.get('second'))
          type = request.POST.get('type')
          description = request.POST.get('description')

          Relationship.objects.create(first_person=first_character,
                                      second_person=second_character,
                                      type=type,
                                      description=description)
          return redirect('character-details', id=id)


# deletes an existing relationship from the database
class DeleteRelationship(View):
    def get(self, request, id, char_id):
        relationship = Relationship.objects.get(pk=id)
        relationship.delete()
        return redirect('character-details', id=char_id)


# edits an existing relationship
class EditRelationship(View):
    def get(self, request, id, char_id):
        relationship = Relationship.objects.get(pk=id)
        all_characters = Character.objects.filter(~Q(pk=id))

        if relationship.first_person.id == char_id:
            character = relationship.first_person
            second_character = relationship.second_person
        else:
            second_character = relationship.first_person
            character = relationship.second_person

        return render(request, 'organizer/edit_relationship.html', {'relationship': relationship, 'all_characters': all_characters,
                                                                    'character': character, 'second_character': second_character})
    def post(self, request, id, char_id):
        relationship = Relationship.objects.get(pk=id)

        second_character = Character.objects.get(pk=request.POST.get('second'))
        type = request.POST.get('type')
        description = request.POST.get('description')

        relationship.second_person = second_character
        relationship.type = type
        relationship.description = description
        relationship.save()

        return redirect('character-details', id=id)


# displays the details of the specified relationship with its description
class RelationshipDetails(View):
    def get(self, request, id, char_id):
        relationship = Relationship.objects.get(pk=id)
        character = Character.objects.get(pk=char_id)
        return render(request, 'organizer/relationship_view.html', {'relationship': relationship, 'character': character})



# deletes a location from the database
class DeleteLocation(View):
    def get(self, request, id):
        location = Location.objects.get(pk=id)
        location.delete()
        return redirect('locations')


# displays the details about the specified location
class ShowLocationDetails(View):
    def get(self, request, id):
        location = Location.objects.get(pk=id)

        return render(request, 'organizer/location_view.html', {'location': location})


# add a location to the database
class AddLocation(View):
    def get(self, request):
        locations = Location.objects.all()
        characters = Character.objects.all()
        return render(request, 'organizer/create_location.html', {'locations': locations, 'characters': characters})
    def post(self, request):
        name = request.POST.get('name')
        if request.POST.get('parent_location'):
            located_in = Location.objects.get(pk=request.POST.get('parent_location'))
        else:
            located_in = None
        description = request.POST.get('description')
        location_lore = request.POST.get('location_lore')
        gm_notes = request.POST.get('gm_notes')

        Location.objects.create(name=name,
                                parent_location=located_in,
                                description=description,
                                location_lore=location_lore,
                                gm_notes=gm_notes,
                                created_at=datetime.datetime.now(),
                                updated_at=datetime.datetime.now())

        location = Location.objects.last()

        related_characters = request.POST.getlist('related_characters')
        for char in related_characters:
            location.related_characters.add(Character.objects.get(pk=char))
        location.save()

        return redirect('locations')



# edits an existing location through user input
class EditLocation(View):
    def get(self, request, id):
        location = Location.objects.get(pk=id)
        other_locations = Location.objects.filter(~Q(pk=id))
        characters = Character.objects.all()
        return render(request, 'organizer/edit_location.html', {'location': location, 'other_locations': other_locations, 'characters': characters})
    def post(self, request, id):
        location = Location.objects.get(pk=id)
        location.name = request.POST.get('name')
        if request.POST.get('parent_location'):
            location.parent_location = Location.objects.get(pk=request.POST.get('parent_location'))
        else:
            location.parent_location = None
        location.description = request.POST.get('description')
        location.location_lore = request.POST.get('location_lore')
        location.gm_notes = request.POST.get('gm_notes')

        location.updated_at = datetime.datetime.now()

        location.related_characters.clear()
        related_characters = request.POST.getlist('related_characters')
        for char in related_characters:
            location.related_characters.add(Character.objects.get(pk=char))
        location.save()

        return redirect('location-details', id=id)


# displays the list of all events in the game's lore
class LoreEventListView(View):
    def get(self, request):
        events = LoreEvent.objects.all().order_by('name')
        paginator = Paginator(events, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/lore_events.html', {'page_obj': page_obj})
    def post(self, request):
        if 'search' in request.POST:
            search = request.POST.get('searchText')
            events = LoreEvent.objects.filter(name__icontains=search).order_by('name')
        paginator = Paginator(events, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/lore_events.html', {'page_obj': page_obj})



# deletes lore event from the database
class DeleteLoreEvent(View):
    def get(self, request, id):
        event = LoreEvent.objects.get(pk=id)
        event.delete()
        return redirect('lore-events')



# adds a new lore event to the database
class AddLoreEvent(View):
    def get(self, request):
        locations = Location.objects.all()
        characters = Character.objects.all()
        return render(request, 'organizer/create_lore_event.html', {'locations': locations, 'characters': characters})
    def post(self, request):
        name = request.POST.get('name')
        time = request.POST.get('time')
        summary = request.POST.get('summary')
        gm_notes = request.POST.get('gm_notes')
        related_locations = request.POST.getlist('related_locations')
        related_characters = request.POST.getlist('related_characters')

        LoreEvent.objects.create(name=name,
                                 time=time,
                                 summary=summary,
                                 gm_notes=gm_notes,
                                 updated_at=datetime.datetime.now(),
                                 created_at=datetime.datetime.now())

        event = LoreEvent.objects.last()

        for char in related_characters:
            event.related_characters.add(Character.objects.get(pk=char))

        for loc in related_locations:
            event.related_locations.add(Location.objects.get(pk=loc))

        event.save()

        return redirect('lore-events')


# displays details about the specified lore event
class LoreEventDetails(View):
    def get(self, request, id):
        event = LoreEvent.objects.get(pk=id)
        return render(request, 'organizer/lore_event_view.html', {'event': event})


# edits information about the specified lore event
class EditLoreEvent(View):
    def get(self, request, id):
        locations = Location.objects.all()
        characters = Character.objects.all()
        event = LoreEvent.objects.get(pk=id)
        return render(request, 'organizer/edit_lore_event.html', {'locations': locations, 'event': event, 'characters': characters})
    def post(self, request, id):
        event = LoreEvent.objects.get(pk=id)
        event.name = request.POST.get('name')

        event.time = request.POST.get('time')
        event.summary = request.POST.get('summary')
        event.gm_notes = request.POST.get('gm_notes')

        event.updated_at = datetime.datetime.now()

        event.related_characters.clear()
        event.related_locations.clear()
        related_characters = request.POST.getlist('related_characters')
        related_locations = request.POST.getlist('related_locations')

        for char in related_characters:
            event.related_characters.add(Character.objects.get(pk=char))

        for loc in related_locations:
            event.related_locations.add(Location.objects.get(pk=loc))

        event.save()

        return redirect('lore-event-details', id=id)


# displays the list of all campaign events, sorted chronologically according to their internal logic
class CampaignEventListView(View):
    def get(self, request):
        if CampaignEvent.objects.count() > 0:
            events_list = [CampaignEvent.objects.filter(previous_event=None).first()]
            current_event = events_list[0]

            for i in range(CampaignEvent.objects.count()-1):
                events_list.append(CampaignEvent.objects.filter(previous_event=current_event).first())
                current_event = events_list[-1]

        else:
            events_list = []
        paginator = Paginator(events_list, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/campaign_events.html', {'page_obj': page_obj})

    def post(self, request):
        if CampaignEvent.objects.count() > 0:
            events_list = [CampaignEvent.objects.filter(previous_event=None).first()]
            current_event = events_list[0]

            for i in range(CampaignEvent.objects.count()-1):
                events_list.append(CampaignEvent.objects.filter(previous_event=current_event).first())
                current_event = events_list[-1]

        else:
            events_list = []

        if 'search' in request.POST:
            search = request.POST.get('searchText')
            filtered_events = CampaignEvent.objects.filter(name__icontains=search)
            for event in events_list:
                if event not in filtered_events:
                    events_list.remove(event)

        paginator = Paginator(events_list, 25)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'organizer/campaign_events.html', {'page_obj': page_obj})


# removes the specified campaign event from the database
class DeleteCampaignEvent(View):
    def get(self, request, id):
        event = CampaignEvent.objects.get(pk=id)
        prev_event = event.previous_event
        next_event = CampaignEvent.objects.filter(previous_event=event).first()
        event.delete()

        if next_event:
            next_event.previous_event = prev_event
            next_event.save()


        return redirect('campaign-events')

# displays the details about the specified campaign event
class CampaignEventDetails(View):
    def get(self, request, id):
        event = CampaignEvent.objects.get(pk=id)
        return render(request, 'organizer/campaign_event_view.html', {'event': event})


# adds a new campaign events chronologically between existing events
class AddCampaignEventAbove(View):
    def get(self, request, id):
        return render(request, 'organizer/create_campaign_event.html')
    def post(self, request, id):
        event = CampaignEvent.objects.get(pk=id)
        prev_event = event.previous_event

        name = request.POST.get('name')
        summary = request.POST.get('summary')
        gm_notes = request.POST.get('gm_notes')

        event.previous_event = None

        CampaignEvent.objects.create(name=name,
                                     summary=summary,
                                     gm_notes=gm_notes,
                                     previous_event=None,
                                     updated_at=datetime.datetime.now(),
                                     created_at=datetime.datetime.now())

        new_event = CampaignEvent.objects.last()
        event.previous_event = new_event
        event.save()
        new_event.previous_event = prev_event
        new_event.save()



        return redirect('campaign-events')


class EditCampaignEvent(View):
    def get(self, request, id):
        event = CampaignEvent.objects.get(pk=id)
        return render(request, 'organizer/edit_campaign_event.html', {'event': event})
    def post(self, request, id):
        event = CampaignEvent.objects.get(pk=id)
        event.name = request.POST.get('name')

        event.summary = request.POST.get('summary')
        event.gm_notes = request.POST.get('gm_notes')

        event.updated_at = datetime.datetime.now()

        event.save()

        return redirect('campaign-event-details', id=id)


# adds a new campaign event as the last in chronological order
class AddCampaignEventEnd(View):
    def get(self, request):
        return render(request, 'organizer/create_campaign_event.html')
    def post(self, request):
        name = request.POST.get('name')
        summary = request.POST.get('summary')
        gm_notes = request.POST.get('gm_notes')

        if CampaignEvent.objects.count() > 0:
            events_list = [CampaignEvent.objects.filter(previous_event=None).first()]
            current_event = events_list[0]

            for i in range(CampaignEvent.objects.count()-1):
                events_list.append(CampaignEvent.objects.filter(previous_event=current_event).first())
                current_event = events_list[-1]

        else:
            current_event = None

        CampaignEvent.objects.create(name=name,
                                     summary=summary,
                                     gm_notes=gm_notes,
                                     updated_at=datetime.datetime.now(),
                                     created_at=datetime.datetime.now(),
                                     previous_event=current_event)

        return redirect('campaign-events')
