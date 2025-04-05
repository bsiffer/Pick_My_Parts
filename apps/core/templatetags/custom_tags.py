from django import template
from apps.core.templatetags.custom_filters import format_cpu, format_motherboard, format_gpu, format_ram, \
    format_storage, format_computer_case, format_cooling_accessory

register = template.Library()

FORMATTERS = {
    "format_cpu": format_cpu,
    "format_motherboard": format_motherboard,
    "format_gpu": format_gpu,
    "format_ram": format_ram,
    "format_storage": format_storage,
    "format_computer_case": format_computer_case,
    "format_cooling_accessory": format_cooling_accessory,
}

@register.simple_tag
def apply_formatter(item, formatter_name):
    try:
        formatter = FORMATTERS.get(formatter_name)
        if callable(formatter):
            return formatter(item)
        else:
            return item
    except Exception as e:
        return item