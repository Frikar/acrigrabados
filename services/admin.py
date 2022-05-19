from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'preview')
    prepopulated_fields = {"slug": ("name",)}

    def preview(self,obj):
        if obj.image:
            return format_html('<img src="{0}" style="width: 100px; height:100px;" />'.format(f'/media/{obj.image}'))
        else:
            return "Sin imagen"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["name"].label = "Nombre de la categoría:"
        form.base_fields["image"].label = "Imagen de la categoría:"
        return form

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'category', 'slug', 'preview')
    prepopulated_fields = {"slug": ("name",)}
    list_filter=['category']
    search_fields=['category']

    def preview(self,obj):
        if obj.image:
            return format_html('<img src="{0}" style="width: 100px; height:100px;" />'.format(f'/media/{obj.image}'))
        else:
            return "Sin imagen"
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["name"].label = "Nombre del producto con codigo:"
        form.base_fields["image"].label = "Imagen del producto:"
        form.base_fields["content"].label = "Contenido del producto:"
        form.base_fields["category"].label = "Categoría del producto:"
        return form

admin.site.register(Product, ProductAdmin)