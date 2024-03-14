# Generated by Django 5.0.2 on 2024-03-14 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouthSpotsBrain', '0001_initial'),
        ('meetup', '0003_alter_meetups_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetups',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='YouthSpotsBrain.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetups',
            name='visibility',
            field=models.CharField(choices=[('-', 'Private'), ('+', 'Public'), ('#', 'Protected')], default='Private', max_length=10),
        ),
    ]
