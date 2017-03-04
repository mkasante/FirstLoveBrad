from django import template
import re

register = template.Library()

@register.filter(name='length_is_gt', is_safe=False)
def length_is_gt(text, value):
	return len(str(text)) > value

@register.filter(name='length_is_gt', is_safe=False)
def length_is_gt(text, value):
	return len(str(text)) > value

@register.filter(name='regex_validates', is_safe=False)
def regex_validates(text, value):
	return re.findall(value, text)
