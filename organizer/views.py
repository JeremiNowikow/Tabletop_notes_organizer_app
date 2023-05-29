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


class EditRelationship(View):
    def get(self, request, id):
        relationship = Relationship.objects.get(pk=id)
        return render(request, 'organizer/edit_relationship.html', {'relationship': relationship})


class DeleteLocation(View):
    def get(self, request, id):
        location = Location.objects.get(pk=id)
        location.delete()
        return redirect('locations')

class ShowLocationDetails(View):
    def get(self, request, id):
        location = Location.objects.get(pk=id)

        return render(request, 'organizer/location_view.html', {'location': location})
