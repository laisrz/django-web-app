# Generated by Django 5.0.4 on 2024-04-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_category_name_alter_collection_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductItem',
        ),
    ]
