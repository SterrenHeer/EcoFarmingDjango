# Generated by Django 5.0.7 on 2024-08-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_farming', '0021_alter_publication_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='description_2',
            field=models.TextField(blank=True, verbose_name='Описание (дополнительное)'),
        ),
    ]
