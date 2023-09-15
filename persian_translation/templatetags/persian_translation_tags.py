from django import template
from persian_tools import separator

register = template.Library()


@register.filter
def translate_number(value):
    value = str(value)
    english_to_persian = value.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return value.translate(english_to_persian)


@register.filter
def number_separator(value):
    return separator.add(value)
