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
        nhoods = Neighbourhood.get_nhoods()
        return render(request, 'index.html', {"form":form,"nhoods":nhoods})
    return render(request, 'index.html', {"form":form,"nhoods":nhoods})
