import datetime

import pytest
from django.contrib.auth.models import User

from organizer.models import Character, PlayerCharacter, NonPlayableCharacter, Relationship, Location, LoreEvent


@pytest.fixture
def characters_fixt():
    char_list = []
    now = datetime.datetime.now()
    char_list.append(PlayerCharacter.objects.create(name='One', short_description="Desc", created_at=now, updated_at=now))
    char_list.append(NonPlayableCharacter.objects.create(name='Two', short_description="Desc", created_at=now, updated_at=now))
    char_list.append(PlayerCharacter.objects.create(name='Three', short_description="Desc", created_at=now, updated_at=now))
    return char_list

@pytest.fixture
def user_fixt():
    u = User.objects.create(username='test')
    return u

@pytest.fixture
def relationship_fixt(characters_fixt):
    return Relationship.objects.create(first_person=characters_fixt[0], second_person=characters_fixt[1], type='friends', description='desc')

@pytest.fixture
def locations_fixt():
    loc_list = []
    now = datetime.datetime.now()
    loc_list.append(Location.objects.create(name='Location1', description='Desc', created_at=now, updated_at=now))
    loc_list.append(Location.objects.create(name='Location2', description='Desc', created_at=now, updated_at=now))
    loc_list.append(Location.objects.create(name='Location3', description='Desc', created_at=now, updated_at=now))
    return loc_list

@pytest.fixture
def lore_events_fixt():
    lore_list = []
    now = datetime.datetime.now()
    lore_list.append(LoreEvent.objects.create(name='Event1', summary='Summary1', created_at=now, updated_at=now))
    lore_list.append(LoreEvent.objects.create(name='Event2', summary='Summary2', created_at=now, updated_at=now))
    lore_list.append(LoreEvent.objects.create(name='Event3', summary='Summary3', created_at=now, updated_at=now))

    return lore_list
