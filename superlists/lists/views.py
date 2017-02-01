from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Item, List


def home_page(request):
    return render(request, 'lists/home.html', {'title': 'To-Do'})


def lists_view(request, list_id):
    return render(request, 'lists/list.html', {
        'title': 'To-Do List',
        'items': Item.objects.filter(todo_list_id=list_id),
        'list_id': list_id,
    })


@require_POST
def new_item(request):
    a_list = List.objects.create()
    Item.objects.create(
        text=request.POST.get('item_text'),
        todo_list=a_list
    )
    return redirect(
        reverse(lists_view, kwargs={'list_id': a_list.id})
    )


@require_POST
def add_item(request, list_id):
    Item.objects.create(text=request.POST.get('item_text'),
                        todo_list_id=list_id)
    return redirect(
        reverse(lists_view, kwargs={'list_id': list_id})
    )
