from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.


# Abstract model from which the PlayerCharacter and NonPlayableCharacter models inherit
class Character(PolymorphicModel):
    name = models.CharField(max_length=128)
    short_description = models.TextField()
    backstory = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    race = models.CharField(max_length=128, blank=True, null=True)
    # Game master's private notes about the character, not viewable by the player users
    gm_notes = models.TextField(blank=True, null=True)
    appearance_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='relations')

    def __str__(self):
        return f"{self.name}: {self.short_description}"



class PlayerCharacter(Character):
    player = models.CharField(max_length=128)
    character_class = models.CharField(max_length=128, blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    character_sheet = models.ImageField(blank=True, null=True)


class NonPlayableCharacter(Character):
    statblock = models.ImageField(blank=True, null=True)
    history_with_players = models.TextField(blank=True, null=True)


# stores relationship between two characters
class Relationship(models.Model):
    first_person = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="from_rel")
    second_person = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="to_rel")
    name = models.CharField(max_length=128)  # eg. "lovers", "sworn enemies", etc.
    description = models.TextField(blank=True, null=True)


class Location(models.Model):
    name = models.CharField(max_length=128)

    # eg. the kingdom in which a city is located in
    parent_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    # any characters living in the location or that have a history with it
    related_characters = models.ManyToManyField(Character, blank=True)
    description = models.TextField(null=True, blank=True)

    # Game master's private notes about the location, not viewable by the player users
    gm_notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


# event that happened in the history of the game's world
class LoreEvent(models.Model):
    name = models.CharField(max_length=128)

    # Not as DateTimeField, since it can include unspecified time periods or fantasy dates
    time = models.CharField(max_length=128, blank=True, null=True)
    summary = models.TextField(null=True, blank=True)

    # characters connected to the event in some way
    related_characters = models.ManyToManyField(Character, blank=True)

    #locations connected to the event in some way
    related_locations = models.ManyToManyField(Location, blank=True)

    # Game master's private notes about the event, not viewable by the player users
    gm_notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


# what happened during the actual game with the players, basically to help write a summary of events so far
class CampaignEvent(models.Model):
    name = models.CharField(max_length=128)
    summary = models.TextField(null=True, blank=True)

    # points to the previous event in the story, helping to form a timeline of events
    previous_event = models.OneToOneField('self', null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()