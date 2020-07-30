# Generated by Django 3.0.8 on 2020-07-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200728_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='home_address_city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='mailing_address_city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='client_rating',
            field=models.CharField(choices=[(None, 'Unknown - (No Data Avaiable from any source)'), (1, 'Very Poor - Required to pay a fee or deposit'), (2, 'Fair - Subprime borrower, require higher down payment'), (3, 'Good - Offer unfavorable terms (i.e. low down-payment)'), (4, 'Very Good - Offer favorable terms on credit accounts'), (5, 'Exceptional - Top of the list offer the best rates')], default='Unknown - (No Data Avaiable from any source)', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='client_token',
            field=models.CharField(default='Fj7UsXaZr6GAOjBZFLgBdlnVB96dxxtlmPi2VbISNtLY1vEqZn', max_length=52),
        ),
    ]