# Generated by Django 4.2.4 on 2023-12-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerceapp', '0006_remove_cartitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='locality',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pin',
            field=models.IntegerField(null=True),
        ),
    ]
