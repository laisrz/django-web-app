# Generated by Django 5.0.4 on 2024-04-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_customer_address_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_complemento',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
