from django.shortcuts import render
from .models import Category, Product


# Create your views here.
def services(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, 'services/services.html', context)


def category(request, slug):
    categories = Category.objects.all().order_by('name')
    obj = Category.objects.get(slug=slug)
    context = {"category": obj, "categories": categories}
    return render(request, 'services/category.html', context)
