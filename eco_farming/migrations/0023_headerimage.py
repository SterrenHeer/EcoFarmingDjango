# Generated by Django 5.0.7 on 2024-08-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0022_publication_description_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Адрес страницы')),
                ('image', models.ImageField(upload_to='header_images', verbose_name='Изображение для шапки страницы')),
            ],
        ),
    ]
