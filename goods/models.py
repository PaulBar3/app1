import decimal
from email.mime import image
from tabnanny import verbose
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True,verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True,verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True,verbose_name="Описание")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")


    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    