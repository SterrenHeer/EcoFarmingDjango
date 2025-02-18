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
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField("Изображение", upload_to='product_categories')
    color = models.CharField("Цвет", max_length=100)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_brands', args=[str(self.slug)])


class Brand(models.Model):
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField(null=True, unique=True)
    description = models.TextField("Описание")
    image = models.ImageField("Логотип", upload_to='brand_logos')
    type = models.CharField("Тип продукта", max_length=100)
    substance = models.CharField("Действующее вещество", max_length=100)
    preparative = models.CharField("Препаративная форма", max_length=100)
    consumption = models.CharField("Норма расхода", max_length=100)
    packaging = models.CharField("Упаковка", max_length=100)
    expiration = models.CharField("Срок годности", max_length=100)
    effect = models.TextField("Действие", null=True, blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('brands_details', args=[str(self.product_category.slug), str(self.id)])


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
    saboteur = models.CharField("Вредный объект", max_length=100)
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


class HarmfulCategory(models.Model):
    TYPE_CHOICES = (
        ('Сорняки', 'Сорняки'),
        ('Болезни', 'Болезни'),
        ('Вредители', 'Вредители'),
    )
    title = models.CharField("Название", max_length=100)
    type = models.CharField("Тип", max_length=100, choices=TYPE_CHOICES)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'категория вредных объектов'
        verbose_name_plural = 'Категории вредных объектов'

    def __str__(self):
        return f'{self.title} ({self.type})'

    def get_items(self):
        return self.harmful_set.all()


class Harmful(models.Model):
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField(null=True, unique=True)
    title_latin = models.CharField("Название (лат.)", max_length=100)
    image = models.ImageField("Изображение (главное)", upload_to='harmful_logos')
    description = models.TextField("Описание", max_length=600)
    family = models.CharField("Семейство", max_length=100)
    subtype = models.CharField("Подтип", max_length=100)
    bio_group = models.CharField("Биологическая группа", max_length=100)
    biology = models.TextField("Биология", max_length=400)
    category = models.ForeignKey(HarmfulCategory, on_delete=models.CASCADE, verbose_name="Категория")
    brand = models.ManyToManyField('Brand', verbose_name="Продукты (опционально)", blank=True)

    class Meta:
        verbose_name = 'вредный объект'
        verbose_name_plural = 'Вредные объекты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('harmful_details', args=[str(self.category.slug), str(self.id)])


class HarmfulImage(models.Model):
    harmful = models.ForeignKey(Harmful, on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField("Изображение", upload_to='brand_effect_images')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.harmful.title


class CultureCategory(models.Model):
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField("Изображение", upload_to='culture_categories')
    icon = models.ImageField("Иконка", upload_to='culture_categories')
    description = models.TextField("Описание")
    brand = models.ManyToManyField('Brand', verbose_name="Продукты (опционально)", blank=True)

    class Meta:
        verbose_name = 'категория культур'
        verbose_name_plural = 'Категории культур'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cultures_category_details', args=[str(self.slug), str(self.id)])


class Culture(models.Model):
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField("Изображение", upload_to='culture_items')
    description = models.TextField("Описание")
    category = models.ForeignKey(CultureCategory, on_delete=models.CASCADE, verbose_name="Категория")
    brand = models.ManyToManyField('Brand', verbose_name="Продукты (опционально)", blank=True)

    class Meta:
        verbose_name = 'культура'
        verbose_name_plural = 'Культуры'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('culture_details', args=[str(self.category.slug), str(self.slug), str(self.id)])


class PublicationCategory(models.Model):
    title = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = 'категория публикаций'
        verbose_name_plural = 'Категории публикаций'

    def __str__(self):
        return self.title


class Publication(models.Model):
    TYPE_CHOICES = (
        ('Наука', 'Наука'),
        ('Публикации', 'Публикации'),
        ('Видеоматериалы', 'Видеоматериалы'),
    )
    type = models.CharField("Тип публикации", max_length=100, choices=TYPE_CHOICES)
    title = models.CharField("Заголовок", max_length=100)
    slug = models.SlugField(null=True)
    image = models.ImageField("Изображение (главное) или превью видео", upload_to='publications_main_images')
    video = models.FileField(upload_to="publications_videos", blank=True)
    description = models.TextField("Описание", max_length=600)
    description_2 = models.TextField("Описание (дополнительное)", blank=True)
    date = models.DateField("Дата размещения")
    category = models.ForeignKey(PublicationCategory, on_delete=models.CASCADE, verbose_name="Категория публикации")

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication_details', args=[str(self.slug), str(self.id)])


class PublicationImage(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name="Публикация")
    image = models.ImageField("Изображение", upload_to='publications_images')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.publication.title


class HeaderImage(models.Model):
    title = models.CharField("Название страницы", max_length=100)
    path = models.CharField("Адрес страницы", max_length=300)
    image = models.ImageField("Изображение для шапки страницы", upload_to='header_images')

    class Meta:
        verbose_name = 'изображение для шапки страницы'
        verbose_name_plural = 'Изображения для шапок страниц'

    def __str__(self):
        return self.title


class ContactsPage(models.Model):
    phone_numbers = models.TextField("Телефоны для связи:", max_length=600)
    email = models.EmailField("Почта:", max_length=254)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = 'страница контактов'
        verbose_name_plural = 'Страница контактов'

    def __str__(self):
        return 'Страница контактов'


class CompanyPage(models.Model):
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='company_images')
    description_2 = models.TextField("Описание")

    class Meta:
        verbose_name = 'страница компании'
        verbose_name_plural = 'Страница компании'

    def __str__(self):
        return 'Страница компании'


class ContactsPageItem(models.Model):
    page = models.ForeignKey(ContactsPage, on_delete=models.CASCADE, verbose_name="Страница")
    title = models.CharField("Наименование", max_length=200)
    description = models.TextField("Контактные данные", max_length=600)
    phone_number = models.CharField("Номер телефона", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'контактное лицо'
        verbose_name_plural = 'контактные лица'

    def __str__(self):
        return self.title
