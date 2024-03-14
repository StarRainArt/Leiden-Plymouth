# Generated by Django 5.0.2 on 2024-03-14 10:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('YouthSpotsBrain', '0002_pins_pin_type_alter_profile_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=200)),
                ('name_meetup', models.CharField(default='There is no title', max_length=255)),
                ('description', models.TextField(default='There is no description')),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('tags', models.CharField(default='none', max_length=255)),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.CharField(choices=[('-', 'Private'), ('+', 'Public'), ('#', 'Protected')], default='Private', max_length=10)),
                ('invited', models.ManyToManyField(related_name='invited', to='YouthSpotsBrain.profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YouthSpotsBrain.profile')),
                ('pin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='YouthSpotsBrain.pins')),
            ],
            options={
                'ordering': ['-created_timestamp'],
            },
        ),
    ]
