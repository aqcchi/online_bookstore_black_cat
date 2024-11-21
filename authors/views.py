from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from authors.forms import AuthorEditForm, AuthorAddForm
from authors.models import Author


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors/authors-list.html'


class AuthorAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Author
    form_class = AuthorAddForm
    template_name = 'authors/author-add.html'
    success_url = reverse_lazy('authors-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AuthorEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/author-edit.html'

    def get_success_url(self):
        # redirecting to the author details page for the current book
        return reverse_lazy('author-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Author
    template_name = 'authors/author-delete.html'
    success_url = reverse_lazy('authors-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AuthorsDetailView(DetailView):
    model = Author
    template_name = 'authors/author-details.html'
    context_object_name = 'author'

