from django import template
import random

register = template.Library()

@register.filter
def last_octet(ip_address):
    try:
        return int(ip_address.split('.')[-1]) * 3 % 360
    except ValueError:
        return 0
    
