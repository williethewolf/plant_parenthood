import re
#import time and date utils from django
from django.utils import timezone
#import templates to gnerate a tag to use anywhere in the site
from django import template
register = template.Library()

#get today's date and pass as a custom template tag
@register.simple_tag
def days_until(date, watertime):
    delta = today_date() - date
    return watertime-delta.days

@register.simple_tag
def today_date():
     return timezone.now().date()

@register.filter(name='times') 
def times(number):
    return range(number)