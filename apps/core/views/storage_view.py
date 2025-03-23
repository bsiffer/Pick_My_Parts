from django.shortcuts import redirect, render
from apps.core.forms.storage_form import StorageForm
from apps.core.models.storage import Storage

def storage_view(request):
    storage_form = StorageForm()

    if request.method == 'POST':
        if 'create_storage' in request.POST:
            storage_form = StorageForm(request.POST)
            print(storage_form.data)
            print(storage_form.errors)
            if storage_form.is_valid():
                storage_form.save()
                return redirect('All Storages')

    all_storage_devices = Storage.objects.all()

    return render(request, 'core/storage.html', {
        'storage_form': storage_form,
        'storages': all_storage_devices,
    })