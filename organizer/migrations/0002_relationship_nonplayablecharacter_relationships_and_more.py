# Generated by Django 4.2.1 on 2023-05-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='nonplayablecharacter',
            name='relationships',
            field=models.ManyToManyField(related_name='relations', through='organizer.Relationship', to='organizer.nonplayablecharacter'),
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='relationships',
            field=models.ManyToManyField(related_name='relations', through='organizer.Relationship', to='organizer.playercharacter'),
        ),
    ]
