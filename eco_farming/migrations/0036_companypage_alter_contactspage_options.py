# Generated by Django 5.0.7 on 2024-08-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0035_contactspage_contactspageitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='company_images', verbose_name='Изображение')),
                ('description_2', models.TextField(max_length=3000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'страница компании',
                'verbose_name_plural': 'Страница компании',
            },
        ),
        migrations.AlterModelOptions(
            name='contactspage',
            options={'verbose_name': 'страница контактов', 'verbose_name_plural': 'Страница контактов'},
        ),
    ]
