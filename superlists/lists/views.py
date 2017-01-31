from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item


def home_page(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text)
        return redirect(reverse(lists_view))
    return render(request, 'lists/home.html', {
        'title': 'To-Do',
        'items': Item.objects.all(),
    })


def lists_view(request):
    return render(request, 'lists/list.html', {
        'title': 'To-Do List',
        'items': Item.objects.all(),
    })


def new_item(request):
    pass
