from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'blog_entries'

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'   

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title','entry_text']    

    def form_valid(self,form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)