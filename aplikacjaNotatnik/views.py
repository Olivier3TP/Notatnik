from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm, EditNoteForm

# Create your views here.
# def notes_list(request):
#     notes = Note.objects.all()
#     return render(request, "notes.list.html", {"notes": notes})
def index(request):
    notes = Note.objects.all()
    return render(request, index.html, {'notes': notes})

def notes_list(request):
    notes = Note.objects.all()
    paginator = Paginator(notes, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "notes_list.html", {"notes": notes})

def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, "add_note.html", {"form": form})

def detail_note(request, id):
    note = get_object_or_404(Note, pk=id)
    return render(request, "detail_note.html", {"note": note})

def edit_note(request, id):
    note = get_object_or_404(Note, pk=id)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('detail_note', id=note.id)
    else:
        form = EditNoteForm(instance=note)
    return render(request, 'edit_note.html', {"form": form})
