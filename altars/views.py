from django.shortcuts import render, redirect
from .forms import AltarForm
from .models import Altar
from django.contrib import messages

def add_altar(request):
    if request.method == 'POST':
        form = AltarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_altars')
    else:
        form = AltarForm()
    return render(request, 'altars/add_altar.html', {'form': form})


def list_altars(request):
    # Use prefetch_related to retrieve all related contact and event data
    # in a single, optimized set of queries, preventing the N+1 problem.
    altars = Altar.objects.prefetch_related('contact_set', 'event_set').all()
    return render(request, 'altars/list_altars.html', {'altars': altars})



def update_altar(request, altar_id):
    altar = Altar.objects.get(pk=altar_id)
    if request.method == 'POST':
        form = AltarForm(request.POST, instance=altar)
        if form.is_valid():
            form.save()
            return redirect('list_altars')
    else:
        form = AltarForm(instance=altar)
    return render(request, 'altars/update_altar.html', {'form': form})

def delete_altar(request, altar_id):
    altar = Altar.objects.get(pk=altar_id)
    altar.delete()
    messages.success(request, 'Altar deleted successfully.')
    return redirect('list_altars')

def search_altars(request):
    query = request.GET.get('q')
    altars = Altar.objects.filter(name__icontains=query)
    return render(request, 'altars/search_altars.html', {'altars': altars, 'query': query})