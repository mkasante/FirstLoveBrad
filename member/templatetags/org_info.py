from django import template
from welcome.models import Organization

register = template.Library()

@register.simple_tag
def user_info(arg):
	return getattr(Organization.objects.last(), arg, "First Love Church")