# Generated by Django 4.2.11 on 2024-03-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0003_alter_meetupdata_type_meetup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetupdata',
            name='type_meetup',
            field=models.CharField(choices=[('TE', 'Tech Event'), ('EE', 'Entertainment Event'), ('SG', 'Social Gathering'), ('ME', 'Music Event'), ('DE', 'Dance Event'), ('CE', 'Community Event'), ('WC', 'Workshop/Class'), ('FE', 'Fitness Event'), ('VO', 'Volunteer Opportunity'), ('AC', 'Activity Club')], default='CE', max_length=10),
        ),
        migrations.AlterField(
            model_name='meetupdata',
            name='visibility',
            field=models.CharField(choices=[('+', 'Public'), ('-', 'Private'), ('#', 'Protected')], default='-', max_length=10),
        ),
    ]
