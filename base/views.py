from django.shortcuts import render, redirect
from services.models import Category
# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, 'base/home.html', context)

def test(request):
    return render(request, 'index.html')
