# Generated by Django 5.0.4 on 2024-04-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_complemento',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
