# Generated by Django 4.0.1 on 2022-01-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appleapp', '0003_remove_productdetails_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='genres',
            field=models.ManyToManyField(to='appleapp.GenresDetails'),
        ),
    ]