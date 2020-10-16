# Generated by Django 3.1.1 on 2020-09-08 20:34

import budget.models.products
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("description", models.CharField(max_length=200)),
                ("item_size", models.PositiveSmallIntegerField()),
                (
                    "information",
                    models.JSONField(
                        default=budget.models.products.additional_information,
                        verbose_name="Additional Information",
                    ),
                ),
                (
                    "storage_method",
                    models.CharField(
                        choices=[
                            (None, "(Unknown)"),
                            ("ZERO", ""),
                            ("COLD", ""),
                            ("DRY", ""),
                        ],
                        default="(Unknown)",
                        max_length=4,
                    ),
                ),
                (
                    "external_barcode",
                    models.ImageField(
                        upload_to="",
                        verbose_name=budget.models.products.get_or_create_external_barcode,
                    ),
                ),
                (
                    "internal_barcode",
                    models.ImageField(
                        default=budget.models.products.get_or_create_internal_barcode,
                        upload_to="",
                    ),
                ),
                (
                    "img",
                    models.ImageField(
                        default=budget.models.products.get_or_create_product_img,
                        upload_to="",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "contact_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "contact_phone",
                    models.CharField(
                        max_length=12,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number format is 999-999-9999",
                                regex="[0-9]{3}[-]{1}[0-9]{3}[-]{1}[0-9]{4}",
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_deleted", models.DateTimeField()),
                ("total", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="budget.vendor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reorder_level", models.PositiveSmallIntegerField()),
                ("reorder_quantity", models.PositiveSmallIntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="budget.product",
                        to_field="name",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="budget.vendor",
                        to_field="name",
                    ),
                ),
            ],
        ),
    ]