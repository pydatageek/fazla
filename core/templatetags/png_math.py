from django import template

register = template.Library()


@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None


@register.filter
def ratio(value, arg):
    try:
        if value and arg:
            return float(f'{int(value) * 100 / int(arg):.1f}')
        else:
            return None
    except (ValueError, ZeroDivisionError):
        return None
