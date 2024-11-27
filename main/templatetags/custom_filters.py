from django import template

register = template.Library()

@register.filter
def last_six_ip(ip_address):
    parts = ip_address.split('.')
    return f"...{parts[-2]}.{parts[-1]}"