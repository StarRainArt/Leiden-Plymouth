# Generated by Django 4.2.11 on 2024-03-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0014_alter_meetupdata_type_meetup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetupdata',
            name='type_meetup',
            field=models.CharField(choices=[('FE', 'Fitness Event'), ('AC', 'Activity Club'), ('VO', 'Volunteer Opportunity'), ('DE', 'Dance Event'), ('EE', 'Entertainment Event'), ('TE', 'Tech Event'), ('ME', 'Music Event'), ('SG', 'Social Gathering'), ('WC', 'Workshop/Class'), ('CE', 'Community Event')], default='CE', max_length=35),
        ),
        migrations.AlterField(
            model_name='meetupdata',
            name='visibility',
            field=models.CharField(choices=[('-', 'Private'), ('+', 'Public'), ('#', 'Protected')], default='-', max_length=10),
        ),
    ]
