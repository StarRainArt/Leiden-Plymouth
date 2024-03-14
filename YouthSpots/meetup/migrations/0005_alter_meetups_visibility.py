# Generated by Django 5.0.2 on 2024-03-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_meetups_owner_alter_meetups_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetups',
            name='visibility',
            field=models.CharField(choices=[('-', 'Private'), ('#', 'Protected'), ('+', 'Public')], default='Private', max_length=10),
        ),
    ]
