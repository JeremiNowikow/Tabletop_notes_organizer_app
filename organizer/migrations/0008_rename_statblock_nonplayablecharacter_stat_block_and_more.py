# Generated by Django 4.2.1 on 2023-05-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0007_character_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nonplayablecharacter',
            old_name='statblock',
            new_name='stat_block',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='name',
            new_name='type',
        ),
        migrations.AddField(
            model_name='nonplayablecharacter',
            name='role',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
