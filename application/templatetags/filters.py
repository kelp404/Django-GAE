from django import template
from django.utils.html import mark_safe
import json


register = template.Library()

@register.filter(name='json')
def get_json(object):
    return mark_safe(json.dumps(object.__dict__))
