# Tabletop organizer app

***
## Table of contents

* [About](#about)
* [Current features](#features)
* [Technologies](#technologies)
* [Plans for the future](#plans-for-the-future)

***

## About

This app was made to allow a game master running a campaign in a tabletop
role-playing game, such as Dungeons & Dragons or Warhammer Fantasy Roleplay,
to organize their notes regarding their world and the game itself. It is not meant to be 
a toolset to play the games by itself, rather it's a tool that allows the user to avoid
having to go through their months worth of notes just to find specific information about
a character or a location that appeared in their game.

So far, the app allows the user to store information about the characters that
appeared in their game, both those belonging to the players, as well as the so-called NPCs
(non-playable characters). The user can include as little details as just
their name and short description, or add information about their appearance, backstory,
relationships with other characters (stored as a separate model), and more.

Its other features include storing similar kinds of information about the locations
existing in the game's world, and its lore/historical events, with their extent decided
by the user. It also allows the user to create a chronological summary of the
events that happened so far in the campaign.

***

## Technologies

The app was created using:

```
* Python 3.11
* Django 4.2.1
* HTML 5
* Bootstrap 5
```

***

## Plans for the future

There is a lot of room for improvements regarding the functionalities of this app.
So far, my main goals include:
* Improving the login functionalities, so that each user can only edit and delete the data
they created
* Adding a way to store images, so that the user can properly add player character sheets
or NPC stat blocks as image files and display them in the detailed view
of the character.
* Adding a new model for the game world, allowing the users who run campaigns
in more than one tabletop RPG system (for example, Call of Cthulhu and Dungeons & Dragons)
to separately store information about characters, locations, etc. belonging to them.
* Adding a campaign model, for users who run more than one campaign in the same world,
to allow them to create separate summaries of events for each of them.
* Adding new models for custom monsters and religions to allow the user to store
even more information about their game's world
* Improving the visual side of the application, possibly moving away from
Bootstrap.