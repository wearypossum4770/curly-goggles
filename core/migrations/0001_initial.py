# Generated by Django 3.0.8 on 2020-07-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_street_1', models.CharField(max_length=100)),
                ('mailing_street_2', models.CharField(max_length=100)),
                ('mailing_city', models.CharField(max_length=100)),
                ('mailing_state', models.CharField(max_length=2)),
                ('mailing_zip5', models.PositiveIntegerField()),
                ('mailing_zip4', models.PositiveIntegerField()),
            ],
        ),
    ]
