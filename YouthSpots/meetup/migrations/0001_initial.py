# Generated by Django 5.0.2 on 2024-03-14 14:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('YouthSpotsBrain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=200)),
                ('name_meetup', models.CharField(max_length=255)),
                ('description', models.TextField(default='There is no description')),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('tags', models.CharField(default='none', max_length=255)),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.CharField(choices=[('-', 'Private'), ('#', 'Protected'), ('+', 'Public')], default='Private', max_length=10)),
                ('invited', models.ManyToManyField(related_name='invited', to='YouthSpotsBrain.profile')),
                ('pin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='YouthSpotsBrain.pins')),
            ],
            options={
                'ordering': ['-created_timestamp'],
            },
        ),
    ]
