import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe = True) # 注册 template filter
@stringfilter # 希望字符作为字符串
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensiongs.fenced_code', 'markdown.extensions.codehilite'],
        safe_mode = True,
        enable_attributes = False))
