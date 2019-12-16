from django import template

register = template.Library()



@register.filter
def arredonda(values, casas):
    return round(values, casas)