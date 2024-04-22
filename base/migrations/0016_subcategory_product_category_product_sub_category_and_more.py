# Generated by Django 5.0.4 on 2024-04-22 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_category_collection_product_productcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.subcategory'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]