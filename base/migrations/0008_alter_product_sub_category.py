# Generated by Django 5.0.4 on 2024-04-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_product_photo_2_alt_product_photo_3_alt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(choices=[('Calça', 'Calça'), ('Blusa', 'Blusa'), ('Blazer', 'Blazer'), ('Casaco', 'Casaco'), ('Shorts', 'Shorts'), ('Camisa', 'Camisa'), ('Camiseta', 'Camiseta'), ('Moletom', 'Moletom'), ('Saia', 'Saia'), ('Vestido', 'Vestido'), ('Top', 'Top'), ('Legging', 'Legging'), ('Calcinha', 'Calcinha'), ('Cueca', 'Cueca'), ('Pijama', 'Pijama'), ('Meia', 'Meia'), ('Sutiã', 'Sutiã'), ('Bermuda', 'Bermuda'), ('Terno', 'Terno'), ('Anéis', 'Anéis'), ('Bolsas', 'Bolsas'), ('Bonés', 'Bonés'), ('Brincos', 'Brincos'), ('Cachecol', 'Cachecol'), ('Carteiras', 'Carteiras'), ('Cintos', 'Cintos'), ('Colares', 'Colares'), ('Óculos', 'Óculos'), ('Relógios', 'Relógios'), ('Lábios', 'Lábios'), ('Olhos', 'Olhos'), ('Rosto', 'Rosto'), ('Unhas', 'Unhas'), ('Perfume', 'Perfume'), ('Banho', 'Banho'), ('Pós-Banho', 'Pós-Banho')], max_length=50),
        ),
    ]
