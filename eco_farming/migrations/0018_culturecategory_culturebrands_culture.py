# Generated by Django 5.0.7 on 2024-08-02 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0017_remove_harmful_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='product_categories', verbose_name='Изображение')),
                ('icon', models.ImageField(upload_to='culture_categories', verbose_name='Иконка')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория культур',
                'verbose_name_plural': 'Категории культур',
            },
        ),
        migrations.CreateModel(
            name='CultureBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco_farming.brand', verbose_name='Препарат')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco_farming.culturecategory', verbose_name='Культура')),
            ],
            options={
                'verbose_name': 'препарат для категории культур',
                'verbose_name_plural': 'Препараты для категории культур',
            },
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='culture_items', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco_farming.culturecategory', verbose_name='Культура')),
            ],
            options={
                'verbose_name': 'культура',
                'verbose_name_plural': 'Культуры',
            },
        ),
    ]
