<<<<<<< HEAD
# Generated by Django 5.0.2 on 2024-03-12 14:04
=======
# Generated by Django 5.0.2 on 2024-03-12 14:37
>>>>>>> f5edc2840e45a8661a94520a23783799c3c64268

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('meetup', '0007_merge_20240312_1503'),
=======
        ('meetup', '0007_alter_meetupdata_type_meetup_and_more'),
>>>>>>> f5edc2840e45a8661a94520a23783799c3c64268
    ]

    operations = [
        migrations.AlterField(
            model_name='meetupdata',
            name='type_meetup',
<<<<<<< HEAD
            field=models.CharField(choices=[('DE', 'Dance Event'), ('CE', 'Community Event'), ('EE', 'Entertainment Event'), ('AC', 'Activity Club'), ('FE', 'Fitness Event'), ('TE', 'Tech Event'), ('VO', 'Volunteer Opportunity'), ('SG', 'Social Gathering'), ('WC', 'Workshop/Class'), ('ME', 'Music Event')], default='CE', max_length=35),
=======
            field=models.CharField(choices=[('VO', 'Volunteer Opportunity'), ('WC', 'Workshop/Class'), ('DE', 'Dance Event'), ('CE', 'Community Event'), ('SG', 'Social Gathering'), ('TE', 'Tech Event'), ('EE', 'Entertainment Event'), ('AC', 'Activity Club'), ('ME', 'Music Event'), ('FE', 'Fitness Event')], default='CE', max_length=35),
>>>>>>> f5edc2840e45a8661a94520a23783799c3c64268
        ),
        migrations.AlterField(
            model_name='meetupdata',
            name='visibility',
<<<<<<< HEAD
            field=models.CharField(choices=[('#', 'Protected'), ('-', 'Private'), ('+', 'Public')], default='-', max_length=10),
=======
            field=models.CharField(choices=[('#', 'Protected'), ('+', 'Public'), ('-', 'Private')], default='Private', max_length=10),
>>>>>>> f5edc2840e45a8661a94520a23783799c3c64268
        ),
    ]
