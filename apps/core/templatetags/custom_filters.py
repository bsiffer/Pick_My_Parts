from django import template
from django.forms import BooleanField

register = template.Library()

@register.filter
def format_component(component, excluded_fields=None):
    if excluded_fields is None:
        excluded_fields = []

    attributes = [
        f"{field.name}: {getattr(component, field.name)}"
        for field in component._meta.get_fields()
        if field.name not in excluded_fields
        and not field.name.startswith("_")
        and not isinstance(getattr(component, field.name), bool)
    ]
    return " / ".join(attributes)

@register.filter
def format_ram(ram):
    excluded_fields = [field.name for field in ram._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(ram, excluded_fields)

@register.filter
def format_storage(storage):
    excluded_fields = [field.name for field in storage._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(storage, excluded_fields)

@register.filter
def format_computer_case(computer_case):
    excluded_fields = [field.name for field in computer_case._meta.get_fields() if isinstance(field, BooleanField)]
    excluded_fields.append('supported_form_factors')
    return format_component(computer_case, excluded_fields)

@register.filter
def format_cooling_accessory(cooling_accessory):
    excluded_fields = [field.name for field in cooling_accessory._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(cooling_accessory, excluded_fields)

@register.filter
def format_gpu(gpu):
    excluded_fields = [field.name for field in gpu._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(gpu, excluded_fields)

@register.filter
def format_power_supply(power_supply):
    excluded_fields = [field.name for field in power_supply._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(power_supply, excluded_fields)

@register.filter
def format_motherboard(motherboard):
    excluded_fields = [field.name for field in motherboard._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(motherboard, excluded_fields)

@register.filter
def format_cpu(cpu):
    excluded_fields = [field.name for field in cpu._meta.get_fields() if isinstance(field, BooleanField)]
    return format_component(cpu, excluded_fields)