# Generated by Django 3.0.8 on 2020-07-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200730_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='client_token',
            field=models.CharField(default='WGwbRuRZmmgX2ZGPvvRibAcYLkMm45qqIqVlTVS4V2g9VdRYlc', max_length=52),
        ),
    ]
