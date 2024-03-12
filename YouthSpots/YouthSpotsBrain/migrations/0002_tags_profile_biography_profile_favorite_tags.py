# Generated by Django 4.2.11 on 2024-03-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouthSpotsBrain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='There is no name', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(default='There is no biografy', max_length=2000),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_tags',
            field=models.ManyToManyField(related_name='favorite_tags', to='YouthSpotsBrain.tags'),
        ),
    ]
