from django import template
from ..forms import LoginForm

register = template.Library()


@register.inclusion_tag('login.html')
def login():
    return {"form": LoginForm}
