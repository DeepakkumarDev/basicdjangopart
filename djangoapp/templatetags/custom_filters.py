
from django import template

register = template.Library()

@register.filter(name='mul')
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter(name='sub')
def subtract(value, arg):
    try:
        return value - arg
    except (ValueError, TypeError):
        return ''

@register.filter(name='div')
def integer_division(value, arg):
    try:
        return value // arg
    except (ValueError, TypeError):
        return ''
