# Generated by Django 3.0.1 on 2020-01-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auction',
            name='buyout',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auction',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
