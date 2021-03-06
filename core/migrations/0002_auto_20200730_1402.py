# Generated by Django 3.0.8 on 2020-07-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='mailing_state',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='mailing_street_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='mailing_zip4',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='mailing_zip5',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
