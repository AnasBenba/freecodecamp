from django.shortcuts import render, redirect
from django.urls import reverse
from items.models import Item, Category

# Create your views here.
def index(request):
    items = Item.objects.filter(is_solde=False)[0:6]
    categorais = Category.objects.all()
    if items:
        return render(request, 'core/index.html', {
            'items': items,
            'categorais': categorais,
        })
    return render(request, 'core/no_items.html', {'message': 'No items found.'})

def contact(request):
    return render(request, 'core/contact.html')

def redirect_me(request):
    return reverse('contact')