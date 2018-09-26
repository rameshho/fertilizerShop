"""SugureshwaraFertilizerShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from fertilizers import views

urlpatterns = [
    #url('', TemplateView.as_view(template_name='fertilizers/index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    #url('accounts/', include('django.contrib.auth.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^fertilizers/', include('fertilizers.urls', namespace='fertilizers')),
    url(r'^companies/', views.CompanyList.as_view()),
    url(r'^company/(?P<company>[0-9a-zA-Z_-]+)/', views.ProductList.as_view()),
    #url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'),name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)