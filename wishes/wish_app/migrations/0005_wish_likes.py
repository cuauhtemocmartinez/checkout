# Generated by Django 2.2 on 2020-08-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0004_auto_20200830_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='wish_app.User'),
        ),
    ]
