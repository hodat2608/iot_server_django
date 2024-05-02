# filters.py
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def time_display(time_value):

    hours = time_value.hour
    minutes = time_value.minute

    display_string = f"{hours} giờ {minutes} phút"
    return display_string