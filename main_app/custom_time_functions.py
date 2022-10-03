# import re
#import time and date utils from django
from django.utils import timezone as tz
#import templates to gnerate a tag to use anywhere in the site
from django import template
register = template.Library()

#get today's date and pass as a custom template tag
@register.filter(expects_localtime=True)
def days_since(value, arg=None):
    tzinfo = getattr(value, "tzinfo", None)
    try:
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't a date object
        return value
    today = datetime.now(tzinfo).date()
    delta = value - today
    return (abs(delta.days))

@register.simple_tag
def today_date(request):
     return tz.localtime(tz.now()).date()