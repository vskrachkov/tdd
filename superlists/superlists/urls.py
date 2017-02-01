"""
    superlists URL Configuration
    ============================
"""
from django.conf.urls import url, include

import lists.views

urlpatterns = [
    # Home page
    url(r'^$', lists.views.home_page, name='home_page'),

    # Display To-Do list
    url(r'^lists/(?P<list_id>\d+)/$', lists.views.lists_view,
        name='lists_view'),

    # Adds new item to existing to-do list
    url(r'^lists/(?P<list_id>\d+)/add$', lists.views.add_item,
        name='add_new_item'),

    # Creates item in new to-do list
    url(r'^lists/new$', lists.views.new_item, name='new_item'),
]
