# Generated by Django 5.0.7 on 2024-07-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0004_remove_brand_concentration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='consumption',
            field=models.CharField(max_length=100, verbose_name='Норма расхода'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='expiration',
            field=models.CharField(max_length=100, verbose_name='Срок годности'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='packaging',
            field=models.CharField(max_length=100, verbose_name='Упаковка'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='preparative',
            field=models.CharField(max_length=100, verbose_name='Препаративная форма'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='substance',
            field=models.CharField(max_length=100, verbose_name='Действующее вещество'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Тип продукта'),
        ),
    ]
