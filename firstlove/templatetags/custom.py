from django import template

register = template.Library()


# @register.filter(is_safe=False)
# def repl(text):
# 	TEXT = _(text).replace('"', '\\"')
# 	return TEXT