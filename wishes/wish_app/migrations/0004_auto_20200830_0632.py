# Generated by Django 2.2 on 2020-08-30 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0003_grant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='wish_app.Wish'),
        ),
    ]
