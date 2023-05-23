# Generated by Django 4.2.1 on 2023-05-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NonPlayableCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_description', models.TextField()),
                ('backstory', models.TextField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('race', models.CharField(blank=True, max_length=128, null=True)),
                ('gm_notes', models.TextField(blank=True, null=True)),
                ('appearance_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('statblock', models.ImageField(blank=True, null=True, upload_to='')),
                ('history_with_players', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_description', models.TextField()),
                ('backstory', models.TextField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('race', models.CharField(blank=True, max_length=128, null=True)),
                ('gm_notes', models.TextField(blank=True, null=True)),
                ('appearance_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('player', models.CharField(max_length=128)),
                ('character_class', models.CharField(blank=True, max_length=128, null=True)),
                ('level', models.PositiveIntegerField(blank=True, null=True)),
                ('character_sheet', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
