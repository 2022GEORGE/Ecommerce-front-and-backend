# Generated by Django 4.2.4 on 2023-12-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerceapp', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tprice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
