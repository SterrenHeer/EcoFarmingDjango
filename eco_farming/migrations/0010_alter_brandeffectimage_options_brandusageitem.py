# Generated by Django 5.0.7 on 2024-07-31 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0009_alter_productcategory_options_brandeffectimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brandeffectimage',
            options={'verbose_name': 'изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.CreateModel(
            name='BrandUsageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture', models.CharField(max_length=100, verbose_name='Культура')),
                ('saboteur', models.CharField(max_length=100, verbose_name='Вредитель')),
                ('drug_consumption', models.CharField(max_length=100, verbose_name='Норма расхода препарата')),
                ('solution_consumption', models.CharField(max_length=100, verbose_name='Норма расхода рабочего раствора')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eco_farming.brand', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'норма расхода',
                'verbose_name_plural': 'Нормы расхода',
            },
        ),
    ]
