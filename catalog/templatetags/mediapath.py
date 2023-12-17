from django import template

register = template.Library()


@register.filter(is_safe=True)
def mediapath(value):
    """Преобразует заданный путь в полный путь к медиафайлу"""
    if value and hasattr(value, 'url'):
        return value.url
    return value
