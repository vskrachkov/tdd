from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item


def home_page(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text')
        Item.objects.create(text=item_text)
        return redirect(reverse(home_page))
    return render(request, 'lists/home.html', {
        'title': 'To-Do',
        'items': Item.objects.all()
    })
