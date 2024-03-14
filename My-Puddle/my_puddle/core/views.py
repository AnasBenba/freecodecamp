from django.shortcuts import render
from items.models import Item, Category

# Create your views here.
def index(request):
    items = Item.objects.filter(is_solde=False)[0:6]
    if items:
        return render(request, 'core/index.html', {
            'items': items,
        })
    return render(request, 'core/no_items.html', {'message': 'No items found.'})

def contact(request):
    return render(request, 'core/contact.html')