# Generated by Django 5.0.2 on 2024-03-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouthSpotsBrain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meetup_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_meetup', models.CharField(choices=[('FC', 'Fan_cosplay'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FC', max_length=10)),
                ('visiablitie', models.CharField(choices=[('+', 'Public'), ('#', 'Protected'), ('-', 'Private')], default='-', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='meetup_userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='EVCharcinglocation',
        ),
    ]
