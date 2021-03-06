# Generated by Django 3.0.8 on 2020-07-28 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=30)),
                ('mobile_number', models.CharField(blank=True, max_length=12)),
                ('mobile_validated', models.BooleanField(default=False)),
                ('email_validated', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='user_uploads/profile_pics/')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_uploads/avatars/')),
                ('client_token', models.CharField(default='6vofBhGabZk3rItXIPQ59bBkAhhBVOCptHwk2mBChzazu2lGNO', max_length=52)),
                ('user_timezone', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('organization', models.CharField(blank=True, max_length=50)),
                ('mailing_address_street_1', models.CharField(blank=True, max_length=50)),
                ('mailing_address_street_2', models.CharField(blank=True, max_length=50)),
                ('mailing_address_state', models.CharField(blank=True, max_length=50)),
                ('mailing_address_zipcode', models.CharField(blank=True, max_length=10)),
                ('mailing_address_country', models.CharField(blank=True, max_length=50)),
                ('client_rating', models.CharField(choices=[(None, '(No Data Avaiable from any source)'), (1, 'Credit applicants may be required to pay a fee or deposit, and applicants'), (2, 'Considered to be subprime borrower'), (3, 'Offer unfavorable terms (i.e. down-payment)'), (4, 'Offer favorable terms on credit accounts'), (5, 'Top of the list offer the best rates')], default='(No Data Avaiable from any source)', max_length=1)),
                ('home_address_street_1', models.CharField(blank=True, max_length=50)),
                ('home_address_street_2', models.CharField(blank=True, max_length=50)),
                ('home_address_state', models.CharField(blank=True, max_length=50)),
                ('home_address_zipcode', models.CharField(blank=True, max_length=10)),
                ('home_address_country', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
