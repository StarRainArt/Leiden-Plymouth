# Generated by Django 4.2.11 on 2024-03-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_alter_meetupdata_type_meetup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetupdata',
            name='type_meetup',
            field=models.CharField(choices=[('ME', 'Music Event'), ('WC', 'Workshop/Class'), ('VO', 'Volunteer Opportunity'), ('AC', 'Activity Club'), ('TE', 'Tech Event'), ('DE', 'Dance Event'), ('SG', 'Social Gathering'), ('CE', 'Community Event'), ('EE', 'Entertainment Event'), ('FE', 'Fitness Event')], default='CE', max_length=10),
        ),
        migrations.AlterField(
            model_name='meetupdata',
            name='visibility',
            field=models.CharField(choices=[('-', 'Private'), ('#', 'Protected'), ('+', 'Public')], default='-', max_length=10),
        ),
    ]