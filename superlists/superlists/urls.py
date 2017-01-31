"""
    superlists URL Configuration
    ============================
"""
from django.conf.urls import url, include
# from django.contrib import admin

import lists.views

urlpatterns = [
    url(r'^$', lists.views.home_page, name='home_page'),
    url(r'^lists/only-one', lists.views.lists_view, name='lists_view'),
    url(r'^/lists/new', lists.views.new_item, name='new_list'),

    # url(r'^admin/', include(admin.site.urls))
]
