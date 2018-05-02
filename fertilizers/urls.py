from django.conf.urls import url
from . import views

urlpatterns = [
# /fertilizers/
    #url(r'', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexViewCompany.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailViewCompany.as_view(), name='Detail-company'),
    url(r'^Company/add/$', views.CreateViewCompany.as_view(), name='Add-company'),
    url(r'^Company/(?P<pk>[0-9]+)/$', views.UpdateViewCompany.as_view(), name='Update-company'),
    url(r'^Company/(?P<pk>[0-9]+)/delete/$', views.DeleteViewCompany.as_view(), name='Delete-company'),
    url(r'^Company/(?P<pk>[0-9]+)/product/add/$', views.CreateViewProduct.as_view(), name='Add-product'),
    url(r'^Company/(?P<pk>[0-9]+)/product/update/$', views.UpdateViewProduct.as_view(), name='Update-product'),
    url(r'^Company/(?P<pk>[0-9]+)/product/delete/$', views.DeleteViewProduct.as_view(), name='Delete-product'),
]