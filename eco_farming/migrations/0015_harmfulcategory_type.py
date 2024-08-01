# Generated by Django 5.0.7 on 2024-08-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0014_harmfulcategory_alter_harmful_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='harmfulcategory',
            name='type',
            field=models.CharField(choices=[('Сорняки', 'Сорняки'), ('Болезни', 'Болезни'), ('Вредители', 'Вредители')], default='Сорняки', max_length=100, verbose_name='Тип'),
        ),
    ]
