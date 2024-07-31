# Generated by Django 5.0.7 on 2024-07-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=180, verbose_name='Текст слайда')),
                ('image', models.ImageField(blank=True, upload_to='weather_slides', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'слайд в виджете',
                'verbose_name_plural': 'Слайды в виджете',
            },
        ),
    ]
