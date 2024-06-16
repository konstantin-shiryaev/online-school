from django import template
from ..forms import RegisterForm

register=template.Library()

@register.inclusion_tag('register.html')
def sign_up():
    return {"form": RegisterForm}