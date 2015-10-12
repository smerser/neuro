from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime, date

register = template.Library()
    
@register.filter(name='delay')
@stringfilter
def delay(val, arg):
    try:
        a = datetime.strptime(val, "%Y-%m-%d")
        b = datetime.strptime(arg, "%Y-%m-%d")
        return (b-a).days
    except:
        return '---'

