"""This has views for base url"""
from django.views.generic.base import RedirectView

class LoginRedirectView(RedirectView):
    """This will redirect your base url to login page"""
    pattern_name = 'redirect-to-login'
    def get_redirect_url(self, *args, **kwargs):
        return '/login'
