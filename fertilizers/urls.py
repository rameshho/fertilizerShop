from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf.urls.static import static


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
# /fertilizers/
    #url(r'', views.IndexView.as_view(), name='index'),
    #url(r'^$', cache_page(CACHE_TTL)(views.IndexViewCompany.as_view()), name='index'), #with redis cache
    url(r'^$', views.IndexViewCompany.as_view(), name='index'),  #without redis cache
    url(r'^Company/(?P<pk>[0-9]+)/$', views.DetailViewCompany.as_view(), name='Detail-company'),
    url(r'^Company/add/$', views.CreateViewCompany.as_view(), name='Add-company'),
    url(r'^Company/(?P<pk>[0-9]+)/$', views.UpdateViewCompany.as_view(), name='Update-company'),
    url(r'^Company/(?P<pk>[0-9]+)/delete/$', views.DeleteViewCompany.as_view(), name='Delete-company'),
    url(r'^Company/products/(?P<pk>[0-9]+)/$', views.DetailViewProduct.as_view(), name='Detail-product'),
    url(r'^Company/product/add/(?P<pk>[0-9]+)/$', views.CreateViewProduct.as_view(), name='Add-product'),
    url(r'^Company/product/(?P<pk>[0-9]+)/update/$', views.UpdateViewProduct.as_view(), name='Update-product'),
    url(r'^Company/product/(?P<pk>[0-9]+)/delete/$', views.DeleteViewProduct.as_view(), name='Delete-product'),
    url(r'^Company/product/(?P<pk>[0-9]+)/add2/$', views.CreateViewProductDetails.as_view(), name='Add-productdetails'),
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)