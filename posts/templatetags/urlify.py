from urllib import quote_plus
from django import template

register = template.Library()

#register the function as a filter
@register.filter
def urlify(value):
    return quote_plus(value)