# Generated by Django 5.0.4 on 2024-04-29 19:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accueil", "0011_product_discounted_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="stok",
            new_name="stock",
        ),
    ]
