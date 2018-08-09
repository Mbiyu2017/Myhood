from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def join_nhood(request, n_id):
    nhood = Neighbourhood.join_nhood(n_id)
    events = Event.get_events()
    form = EventForm()
    commForm = CommentForm()
    current_user = request.user
    if request.method == 'POST':
        commForm = CommentForm(request.POST)
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.nhood = nhood
            event.poster = current_user
            event.save()
            form = EventForm()
        return render(request, 'nhood.html', {"nhood":nhood,"form":form,"commForm":commForm})
    return render(request, 'nhood.html', {"nhood":nhood,"form":form,"commForm":commForm,"events":events})

@login_required(login_url='/accounts/login/')
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

def search(request):
    if 'term' in request.GET and request.GET['term']:
        term = request.GET.get('term')
        businesses = Business.search_business(term)
        print(businesses,term)
        return render(request, 'search.html',{"businesses":businesses})

def comment(request,event_id):
    if request.method == 'POST':
        commForm = CommentForm()
        comment = commForm.save(commit=False)
        comment.event = Comment.get_comments(event_id)
        comment.save()
        commForm = CommentForm()

        return redirect('join_nhood')
