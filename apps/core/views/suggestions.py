from django.forms import model_to_dict
from django.http import JsonResponse
from django.apps import apps
from apps.core.models.parts_list import PartsList
import json

def get_model_class(request_for_field: str):
    try:
        model_class = apps.get_model('core', request_for_field)
        return model_class
    except LookupError:
        return None

def serialize_part(part):
    """Helper function to serialize a part, including related fields."""
    if hasattr(part, '_meta'):
        part_dict = model_to_dict(part)
        # Serialize related fields like FormFactor
        if 'form_factor' in part_dict:
            if isinstance(part.form_factor, str):
                part_dict['form_factor'] = part.form_factor  # Already a string
            elif part.form_factor:  # If it's an object, get its name
                part_dict['form_factor'] = part.form_factor.name
        if 'supported_form_factors' in part_dict:
            part_dict['supported_form_factors'] = [
                ff.name for ff in part.supported_form_factors.all()
            ]
        return part_dict
    return part

def suggestions(request):
    if request.method == 'GET':
        try:
            # Decode and parse the selectedParts query parameter
            selected_parts_json = request.GET.get('selectedParts', '{}')
            selected_parts = json.loads(selected_parts_json)

            # Get the requestForField query parameter
            request_for_field = request.GET.get('requestForField', None)

            if not request_for_field:
                return JsonResponse({"error": "requestForField is required"}, status=400)

            model_class = get_model_class(request_for_field)

            if not model_class:
                return JsonResponse({"error": f"Model '{request_for_field}' not found"}, status=404)

            # Retrieve all objects of the model: requestForField
            matching_parts = model_class.objects.all()

            # Update selected_parts to include objects from above
            for part in matching_parts:
                if request_for_field not in selected_parts:
                    selected_parts[request_for_field] = []

                if any(existing_part["sku"] == part.sku for existing_part in selected_parts[request_for_field]):
                    continue
                else:
                    selected_parts[request_for_field].append({"sku": part.sku})

            # Create an instance of PartsList and check for compatibility for objects of type requestForField
            parts_list = PartsList()

            for part_type, parts in selected_parts.items():
                model_class = get_model_class(part_type)

                if not model_class:
                    return JsonResponse({"error": f"Model '{part_type}' not found"}, status=404)

                for part in parts:
                    try:
                        # Ensure part_data is a dictionary with "sku"
                        part_object = model_class.objects.get(sku=part["sku"])
                        parts_list.add_part(part_object)
                    except model_class.DoesNotExist:
                        return JsonResponse({"error": f"Part: {model_class} with SKU {part['sku']} not found"}, status=404)

            compatibility_results = parts_list.check_compatibility(request_for_field)

            # Serialize compatible parts
            serialized_parts = [
                serialize_part(part) for part in compatibility_results["compatible_parts"]
            ]

            old_selected_parts = json.loads(selected_parts_json)
            # Remove parts that are already selected
            for old_part in old_selected_parts.get(request_for_field, []):
                serialized_parts = [serialized_part for serialized_part in serialized_parts if old_part["sku"] != serialized_part["sku"]]

            return JsonResponse(serialized_parts, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in selectedParts"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)