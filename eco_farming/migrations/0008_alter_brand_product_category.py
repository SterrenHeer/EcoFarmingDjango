# Generated by Django 5.0.7 on 2024-07-30 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0007_alter_brand_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco_farming.productcategory', verbose_name='Категория'),
        ),
    ]
