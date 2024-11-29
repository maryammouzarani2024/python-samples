from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from guardian.mixins import PermissionRequiredMixin
from .models import Notes
from .forms import NotesForm



class NotesListView(ListView):
    model=Notes
    template_name='notes/list_notes.html'
    context_object_name='notes'
    paginate_by=3
    def get_queryset(self) :
        return Notes.objects.order_by('-created')

class NoteDetailView(DetailView):
    model=Notes
    template_name='notes/detailed_note.html'
    context_object_name='note'
    login_url="/admin"


class NotesCreateView(LoginRequiredMixin,CreateView):
    model=Notes
    template_name="notes/notes_form.html"
    form_class=NotesForm
    success_url='/comments'
    login_url=""

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


 
class NotesUpdateView(PermissionRequiredMixin ,UpdateView):
    model=Notes
    form_class=NotesForm
    success_url="/comments"
    permission_required = 'notes.change_notes'
    raise_exception=True
 
   

class NotesDeleteView(PermissionRequiredMixin,DeleteView):
    model=Notes
    template_name="notes/notes_delete.html"
    success_url='/comments'
    permission_required = 'notes.delete_notes'
    login_url=""
    raise_exception=True