# Generated by Django 5.0.4 on 2024-04-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accueil", "0010_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discounted_price",
            field=models.IntegerField(default=0),
        ),
    ]