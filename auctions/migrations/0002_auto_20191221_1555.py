# Generated by Django 3.0.1 on 2019-12-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auc_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='auction',
            name='bid',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='auction',
            name='buyout',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='auction',
            name='item_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='auction',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
    ]