#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Veris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from django.views.generic import TemplateView


API_TITLE = '{project_name} API'

urlpatterns = [
    # url(r'^swagger/$', get_swagger_view(title=API_TITLE)),
    #
    # url(r'^admin/', admin.site.urls),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^docs/', include_docs_urls(title=API_TITLE, description='')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
