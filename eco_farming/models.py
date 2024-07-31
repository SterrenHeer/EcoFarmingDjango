from django.db import models
from django.urls import reverse


class WeatherSlide(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Текст слайда", max_length=180)
    image = models.ImageField("Изображение", upload_to='weather_slides')

    class Meta:
        verbose_name = 'слайд в виджете'
        verbose_name_plural = 'Слайды в виджете'

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение", upload_to='product_categories')
    color = models.CharField("Цвет", max_length=100)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", max_length=400)
    image = models.ImageField("Логотип", upload_to='brand_logos')
    type = models.CharField("Тип продукта", max_length=100)
    substance = models.CharField("Действующее вещество", max_length=100)
    preparative = models.CharField("Препаративная форма", max_length=100)
    consumption = models.CharField("Норма расхода", max_length=100)
    packaging = models.CharField("Упаковка", max_length=100)
    expiration = models.CharField("Срок годности", max_length=100)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.title



