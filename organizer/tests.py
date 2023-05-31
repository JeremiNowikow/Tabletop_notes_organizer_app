import datetime

import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.test import Client
from django.urls import reverse
from django.test import TestCase

from organizer.models import Character, Relationship


# Create your tests here.

@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_character_list_get(characters_fixt):
    client = Client()
    url = reverse('characters')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['page_obj'].paginator.count == len(characters_fixt)
    for char in characters_fixt:
        assert char in response.context['page_obj']


@pytest.mark.django_db
def test_add_player_character(user_fixt):
    client = Client()
    client.force_login(user_fixt)
    url = reverse('add-player')
    data = {
        'name': 'Name1',
        'player': 'test_player',
        'short_description': 'desc',
        'updated_at': datetime.datetime.now(),
        'created_at': datetime.datetime.now()

    }
    response = client.post(url, data)
    assert response.status_code == 302
    redirect_url = reverse('characters')
    assert response.url.startswith(redirect_url)
    char = Character.objects.get(name='Name1')
    assert char

@pytest.mark.django_db
def test_add_npc_character(user_fixt):
    client = Client()
    client.force_login(user_fixt)
    url = reverse('add-npc')
    data = {
        'name': 'Name1',
        'short_description': 'desc',
        'updated_at': datetime.datetime.now(),
        'created_at': datetime.datetime.now()

    }
    response = client.post(url, data)
    assert response.status_code == 302
    redirect_url = reverse('characters')
    assert response.url.startswith(redirect_url)
    char = Character.objects.get(name='Name1')
    assert char

@pytest.mark.django_db
def test_view_character_details(characters_fixt):
    client = Client()
    url = reverse('character-details', kwargs={'id': characters_fixt[0].id})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_player_character_with_no_user(user_fixt):
    client = Client()
    url = reverse('add-player')
    data = {
        'name': 'Name1',
        'player': 'test_player',
        'short_description': 'desc',
        'updated_at': datetime.datetime.now(),
        'created_at': datetime.datetime.now()

    }
    response = client.post(url, data)
    assert response.status_code == 302
    redirect_url = reverse('main')
    assert response.url.startswith(redirect_url)

@pytest.mark.django_db
def test_delete_character(user_fixt, characters_fixt):
    client = Client()
    client.force_login(user_fixt)
    assert Character.objects.get(pk=characters_fixt[0].id)
    url = reverse('delete-character', kwargs={'id': characters_fixt[0].id})
    response = client.get(url)
    assert response.status_code == 302
    try:
        Character.objects.get(pk=characters_fixt[0].id)
        assert False
    except ObjectDoesNotExist:
        assert True
    redirect_url = reverse('characters')
    assert response.url.startswith(redirect_url)

@pytest.mark.django_db
def test_delete_character_with_no_user(user_fixt, characters_fixt):
    client = Client()
    assert Character.objects.get(pk=characters_fixt[0].id)
    url = reverse('delete-character', kwargs={'id': characters_fixt[0].id})
    response = client.get(url)
    assert response.status_code == 302
    redirect_url = reverse('main')
    assert response.url.startswith(redirect_url)

@pytest.mark.django_db
def test_edit_character(characters_fixt, user_fixt):
    client = Client()
    client.force_login(user_fixt)
    url = reverse('edit-character', kwargs={'id': characters_fixt[0].id})

    data = {
        'name': 'Name4',
        'player': 'test_player2',
        'short_description': 'desc',
        'updated_at': datetime.datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302
    char = Character.objects.get(name='Name4')
    assert char.id == characters_fixt[0].id

@pytest.mark.django_db
def test_add_relationship(characters_fixt, user_fixt):
    client = Client()
    client.force_login(user_fixt)
    url = reverse('add-relationship', kwargs={'id': characters_fixt[0].id})
    data = {
        'second': characters_fixt[1].id,
        'type': 'friends'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Relationship.objects.last().type == 'friends'

@pytest.mark.django_db
def test_delete_relationship(relationship_fixt, characters_fixt, user_fixt):
    client = Client()
    client.force_login(user_fixt)
    url = reverse('delete-relationship', kwargs={'char_id': characters_fixt[0].id, 'id': relationship_fixt.id})
    response = client.get(url)
    assert response.status_code == 302
    try:
        Relationship.objects.get(pk=relationship_fixt.id)
        assert False
    except ObjectDoesNotExist:
        assert True
    redirect_url = reverse('character-details', kwargs={'id': characters_fixt[0].id})
    assert response.url.startswith(redirect_url)

@pytest.mark.django_db
def test_edit_relationship(relationship_fixt, characters_fixt, user_fixt):
    client = Client()
    client.force_login(user_fixt)
    url = reverse('edit-relationship', kwargs={'char_id': characters_fixt[0].id, 'id': relationship_fixt.id})
    data = {
        'second': characters_fixt[1].id,
        'type': 'enemies'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    rel = Relationship.objects.get(type='enemies')
    assert rel.id == relationship_fixt.id

    redirect_url = reverse('character-details', kwargs={'id': characters_fixt[0].id})
    assert response.url.startswith(redirect_url)

@pytest.mark.django_db
def test_relationship_details(relationship_fixt, characters_fixt):
    client = Client()
    url = reverse('relationship-details', kwargs={'id': relationship_fixt.id, 'char_id': characters_fixt[0].id})
    response = client.get(url)
    assert response.status_code == 200

