from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):
    current_user = request.user
    nhoods = Neighbourhood.get_nhoods()
    form = NeighbourhoodForm()
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = current_user
            neighbourhood.save()
            form = NeighbourhoodForm()
        nhoods = Neighbourhood.get_nhoods()
        return render(request, 'index.html', {"form":form,"nhoods":nhoods})
    return render(request, 'index.html', {"form":form,"nhoods":nhoods})

def join_nhood(request, n_id):
    nhood = Neighbourhood.join_nhood(n_id)
    form = EventForm()
    current_user = request.user
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.nhood = nhood
            event.poster = current_user
            event.save()
            form = EventForm()
        return render(request, 'nhood.html', {"nhood":nhood,"form":form})
    return render(request, 'nhood.html', {"nhood":nhood,"form":form})

def userprofile(request):
    current_user = request.user
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.save()
            form = BusinessForm()
        return render(request, 'userprofile.html', {"user":current_user, "form":form})
    return render(request, 'userprofile.html', {"user":current_user, "form":form})
