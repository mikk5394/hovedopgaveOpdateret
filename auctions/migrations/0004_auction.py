# Generated by Django 3.0.1 on 2020-01-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auctions', '0003_delete_auction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('time_left', models.CharField(max_length=50)),
            ],
        ),
    ]
