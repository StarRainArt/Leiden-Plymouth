# Generated by Django 5.0.2 on 2024-03-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetups',
            name='visibility',
            field=models.CharField(choices=[('#', 'Protected'), ('-', 'Private'), ('+', 'Public')], default='Private', max_length=10),
        ),
    ]
