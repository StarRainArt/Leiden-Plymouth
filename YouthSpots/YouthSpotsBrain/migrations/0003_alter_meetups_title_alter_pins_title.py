# Generated by Django 5.0.2 on 2024-03-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouthSpotsBrain', '0002_meetups_pins_created_timestamp_pins_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetups',
            name='title',
            field=models.CharField(default='There is no title', max_length=255),
        ),
        migrations.AlterField(
            model_name='pins',
            name='title',
            field=models.CharField(default='There is no title', max_length=255),
        ),
    ]