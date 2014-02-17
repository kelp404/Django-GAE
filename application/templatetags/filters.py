import json
from django import template
from django.utils.html import mark_safe


register = template.Library()

@register.filter(name='json')
def get_json(object):
    """
    Get the json.
    :param object: The class instance.
    :return: 'json string'
    """
    return mark_safe(json.dumps(object.__dict__))
