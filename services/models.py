from django.db import models


# Create your models here. Modelo de ejemplo usando categorías
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="category", blank=True)

    def __str__(self):
        return self.name

    class Meta:  # new
        ordering = ['name']
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("category", kwargs={"slug": str(self.slug)})

    @property
    def get_products(self):
        return Product.objects.filter(category__name=self.name)


class Product(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="products", blank=True)

    def __str__(self):
        return self.name

    class Meta:  # new
        ordering = ['name']
