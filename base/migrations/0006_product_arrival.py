# Generated by Django 5.0.4 on 2024-04-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='arrival',
            field=models.BooleanField(default=False),
        ),
    ]