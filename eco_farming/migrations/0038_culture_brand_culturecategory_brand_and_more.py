# Generated by Django 5.0.7 on 2024-08-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0037_alter_brand_description_alter_brand_effect_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='brand',
            field=models.ManyToManyField(blank=True, to='eco_farming.brand', verbose_name='Продукты (опционально)'),
        ),
        migrations.AddField(
            model_name='culturecategory',
            name='brand',
            field=models.ManyToManyField(blank=True, to='eco_farming.brand', verbose_name='Продукты (опционально)'),
        ),
        migrations.DeleteModel(
            name='CultureBrands',
        ),
    ]
