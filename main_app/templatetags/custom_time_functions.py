import re
#import time and date utils from django
from datetime import datetime
#import templates to gnerate a tag to use anywhere in the site
from django import template
register = template.Library()

#get today's date and pass as a custom template tag
@register.filter
def days_until(date):
    delta = date - today_date()
    return delta.days

@register.simple_tag
def today_date():
     return datetime.now().date()