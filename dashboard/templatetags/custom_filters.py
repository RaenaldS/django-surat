import os
from django import template

register = template.Library()

@register.filter
def filename(value):
    if not value:  # Cek apakah value kosong atau None
        return None
    return os.path.basename(value)
