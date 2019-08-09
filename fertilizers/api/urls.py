from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.conf.urls import include, url
from fertilizers.api import views


urlpatterns = [
    url(r'^get-api-token/', obtain_auth_token, name='api_token_auth'),
    url(r'^companies', views.CompanyList.as_view()),
    url(r'^company/(?P<company>[0-9a-zA-Z_-]+)', views.ProductList.as_view()),
]





urlpatterns = format_suffix_patterns(urlpatterns)
