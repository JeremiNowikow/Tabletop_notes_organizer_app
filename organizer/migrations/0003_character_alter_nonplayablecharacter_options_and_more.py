# Generated by Django 4.2.1 on 2023-05-23 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('organizer', '0002_relationship_nonplayablecharacter_relationships_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
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
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('relationships', models.ManyToManyField(related_name='relations', through='organizer.Relationship', to='organizer.character')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.AlterModelOptions(
            name='nonplayablecharacter',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='playercharacter',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='age',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='appearance_description',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='backstory',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='gm_notes',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='name',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='race',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='relationships',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='nonplayablecharacter',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='age',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='appearance_description',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='backstory',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='gm_notes',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='id',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='name',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='race',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='relationships',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='playercharacter',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('parent_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizer.location')),
                ('related_characters', models.ManyToManyField(blank=True, null=True, to='organizer.character')),
            ],
        ),
        migrations.AddField(
            model_name='nonplayablecharacter',
            name='character_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organizer.character'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='character_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organizer.character'),
            preserve_default=False,
        ),
    ]
