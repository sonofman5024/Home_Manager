from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter(name='trim')
def trim(text, s=None, e=None, j=None):
    return text[s:e:j]


@register.filter(name='tuc')
def tuc(value, arg):
    return value.replace(arg, '')