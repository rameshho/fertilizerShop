'''
templatetags module
'''

from django import template
register = template.Library()

@register.simple_tag
def go_to_url(url):
    return "window.location='" + url +"'; return false;"