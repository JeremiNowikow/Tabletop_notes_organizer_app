# Generated by Django 4.2.1 on 2023-05-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_rename_description_loreevent_summary_campaignevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
