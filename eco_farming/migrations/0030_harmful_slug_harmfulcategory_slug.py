# Generated by Django 5.0.7 on 2024-08-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0029_brand_effect'),
    ]

    operations = [
        migrations.AddField(
            model_name='harmful',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='harmfulcategory',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
