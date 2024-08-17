from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView
from typing import List


from .models import Notes
from .forms import NotesForm

# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
   # fields = ['title', 'text'] #attributes from model that we want user to fill, old version
    success_url = '/smart/notes' #redirect user to this page once success
    form_class = NotesForm # new version

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes' : all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("note doesn't exist.")

    return render(request, 'notes/notes_detail.html', {'notes': note})

