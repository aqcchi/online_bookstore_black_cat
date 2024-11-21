from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from books.forms import BookAddForm, BookEditForm
from books.models import Book
from common.forms import CreateCommentForm


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)

        # Add custom context data (e.g., a list of books)
        context['welcome_message'] = '''
            <h1>Welcome to our Online Bookstore "The Black Cat"!</h1>
            <p>The bookstore is named after Edgar Allan Poe’s short story of the same name – The Black Cat, and it is the perfect place for curious people who love books... and cats.</p>
            <p>Books and cats... what more does a person need in order to be happy?!</p>
            <p>The bookstore is a small family business that we embarked on with a lot of love and enthusiasm, with the hope that there are still people who prefer physical books over e-readers. Our hopes were fulfilled, and now we are happy to announce we have a large number of regular customers who visit us weekly, even daily.</p>
            <p>We hope you will also become a part of our book-loving family!</p>
            <p>Come visit us! :)</p>
        '''
        # context['books'] = Book.objects.all()  # Fetch all books from the database

        return context


class BooksListView(ListView):
    model = Book
    template_name = 'books-list.html'


class BookAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'books/book-add.html'
    success_url = reverse_lazy('books-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class BookEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookEditForm
    template_name = 'books/book-edit.html'

    def get_success_url(self):
        # redirecting to the book details page for the current book
        return reverse_lazy('book-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book-delete.html'
    success_url = reverse_lazy('books-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class BooksDetailView(DetailView):
    model = Book
    template_name = 'book-details.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_comments'] = context['book'].comments.all()
        context['comment_form'] = CreateCommentForm()
        return context


class SearchResultsListView(ListView):
    model = Book
    template_name = 'search-results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
            )


class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url = 'login'
