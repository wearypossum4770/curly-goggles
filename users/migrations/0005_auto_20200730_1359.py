# Generated by Django 3.0.8 on 2020-07-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200729_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address_city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address_country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address_state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address_street_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address_street_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home_address_zipcode',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mailing_address_city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mailing_address_country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mailing_address_state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mailing_address_street_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mailing_address_street_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mailing_address_zipcode',
        ),
        migrations.AddField(
            model_name='profile',
            name='client_bio',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='client_rating',
            field=models.CharField(choices=[(None, 'Unknown - (No Data Avaiable from any source)'), ('1', 'Very Poor - Required to pay a fee or deposit'), ('2', 'Fair - Subprime borrower, require higher down payment'), ('3', 'Good - Offer unfavorable terms (i.e. low down-payment)'), ('4', 'Very Good - Offer favorable terms on credit accounts'), ('5', 'Exceptional - Top of the list offer the best rates')], default='Unknown - (No Data Avaiable from any source)', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='client_token',
            field=models.CharField(default='1BORopQbyt2lFoqhKEJbxHGe7pA7zlLhobhm6l1dsvZJgW8sFg', max_length=52),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
