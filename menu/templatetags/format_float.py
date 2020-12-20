from django import template

register = template.Library()


@register.filter
def format_float(x):
    return "{:.2f}".format(x)
