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

    class Meta:
        verbose_name = 'категория препаратов'
        verbose_name_plural = 'Категории препаратов'

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

    def get_absolute_url(self):
        return reverse('brands_details', args=[str(self.id), str(self.product_category.title)])


class BrandEffectImage(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField("Изображение", upload_to='brand_effect_images')

    class Meta:
        verbose_name = 'действие препарата'
        verbose_name_plural = 'Действие препарата'

    def __str__(self):
        return self.brand.title


class BrandUsageItem(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Товар")
    culture = models.CharField("Культура", max_length=100)
    saboteur = models.CharField("Вредитель", max_length=100)
    drug_consumption = models.CharField("Норма расхода препарата", max_length=100)
    solution_consumption = models.CharField("Норма расхода рабочего раствора", max_length=100)

    class Meta:
        verbose_name = 'норма расхода'
        verbose_name_plural = 'Нормы расхода'

    def __str__(self):
        return self.brand.title


class BrandAdvantage(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Товар")
    description = models.CharField("Описание", max_length=400)

    class Meta:
        verbose_name = 'преимущество'
        verbose_name_plural = 'Преимущества препарата'

    def __str__(self):
        return self.brand.title



