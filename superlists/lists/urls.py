from django.conf.urls import url

from . import views

urlpatterns = [
    # Display To-Do list
    url(r'^(?P<list_id>\d+)/$', views.lists_view,
        name='lists_view'),

    # Adds new item to existing to-do list
    url(r'^(?P<list_id>\d+)/add$', views.add_item,
        name='add_new_item'),

    # Creates item in new to-do list
    url(r'^new$', views.new_item, name='new_item'),
]