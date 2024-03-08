# Generated by Django 5.0.3 on 2024-03-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouthSpotsBrain', '0003_alter_meetups_title_alter_pins_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pins',
            name='invited',
        ),
        migrations.RemoveField(
            model_name='pins',
            name='owner_id',
        ),
        migrations.AddField(
            model_name='meetups',
            name='tags',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='pins',
            name='tags',
            field=models.CharField(default='none', max_length=255),
        ),
    ]