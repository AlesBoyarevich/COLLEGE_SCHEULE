from django import template

register = template.Library()

@register.simple_tag(takes_context=True, name='active')
def active(context, active_name: str):
    ACTIVE_CLASS = 'menu-links-link-active'

    if context['active'] == active_name:
        return ACTIVE_CLASS
    return ''