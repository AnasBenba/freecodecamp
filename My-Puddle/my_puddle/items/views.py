from django.shortcuts import render
from .models import Item

# Create your views here.

def details(request, pk):
    item = Item.objects.filter(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return (request, "item/details.html", {
        "item": item,
        "related_items": related_items,
    })
