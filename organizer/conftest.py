import datetime

import pytest
from django.contrib.auth.models import User

from organizer.models import Character, PlayerCharacter, NonPlayableCharacter

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