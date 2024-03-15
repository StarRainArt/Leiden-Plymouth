# Generated by Django 4.2.11 on 2024-03-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0011_alter_meetupdata_type_meetup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetupdata',
            name='type_meetup',
            field=models.CharField(choices=[('VO', 'Volunteer Opportunity'), ('TE', 'Tech Event'), ('SG', 'Social Gathering'), ('EE', 'Entertainment Event'), ('WC', 'Workshop/Class'), ('ME', 'Music Event'), ('DE', 'Dance Event'), ('CE', 'Community Event'), ('FE', 'Fitness Event'), ('AC', 'Activity Club')], default='CE', max_length=35),
        ),
        migrations.AlterField(
            model_name='meetupdata',
            name='visibility',
            field=models.CharField(choices=[('#', 'Protected'), ('-', 'Private'), ('+', 'Public')], default='-', max_length=10),
        ),
    ]
