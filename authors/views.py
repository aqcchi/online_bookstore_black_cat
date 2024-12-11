from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from authors.forms import AuthorEditForm, AuthorAddForm
from authors.models import Author
from common.mixins import StaffOrSuperuserMixin


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors/authors-list.html'


class AuthorAddView(LoginRequiredMixin, StaffOrSuperuserMixin, CreateView):
    model = Author
    form_class = AuthorAddForm
    template_name = 'authors/author-add.html'
    success_url = reverse_lazy('authors-list')


class AuthorEditView(LoginRequiredMixin, StaffOrSuperuserMixin, UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/author-edit.html'

    def get_success_url(self):
        return reverse_lazy('author-details', kwargs={'pk': self.object.pk})


class AuthorDeleteView(LoginRequiredMixin, StaffOrSuperuserMixin, DeleteView):
    model = Author
    template_name = 'authors/author-delete.html'
    success_url = reverse_lazy('authors-list')


class AuthorsDetailView(DetailView):
    model = Author
    template_name = 'authors/author-details.html'
    context_object_name = 'author'

