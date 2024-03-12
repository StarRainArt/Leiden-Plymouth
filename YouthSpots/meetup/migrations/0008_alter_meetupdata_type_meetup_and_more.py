# Generated by Django 5.0.2 on 2024-03-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0007_alter_meetupdata_type_meetup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetupdata',
            name='type_meetup',
            field=models.CharField(choices=[('VO', 'Volunteer Opportunity'), ('WC', 'Workshop/Class'), ('DE', 'Dance Event'), ('CE', 'Community Event'), ('SG', 'Social Gathering'), ('TE', 'Tech Event'), ('EE', 'Entertainment Event'), ('AC', 'Activity Club'), ('ME', 'Music Event'), ('FE', 'Fitness Event')], default='CE', max_length=35),
        ),
        migrations.AlterField(
            model_name='meetupdata',
            name='visibility',
            field=models.CharField(choices=[('#', 'Protected'), ('+', 'Public'), ('-', 'Private')], default='Private', max_length=10),
        ),
    ]
