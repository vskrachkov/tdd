"""
    superlists URL Configuration
    ============================
"""
from django.conf.urls import url, include

import lists.views

urlpatterns = [
    # Home page
    url(r'^$', lists.views.home_page, name='home_page'),

    # Lists app
    url(r'^lists/', include('lists.urls'))
]
