import datetime
from django.utils import timezone
from django import template
import requests
from urllib.request import urlopen
from django.utils.safestring import mark_safe
from django.utils.html import format_html


register = template.Library()

# @register.simple_tag
# def include_external(url):
# 	include = requests.get(url)
# 	include_safe = mark_safe(include.text)
# 	return include_safe

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
