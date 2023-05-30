# Generated by Django 4.2.1 on 2023-05-30 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0010_alter_location_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignevent',
            name='gm_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campaignevent',
            name='previous_event',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizer.campaignevent'),
        ),
    ]
