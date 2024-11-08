from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from books.models import Book


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)

        # Add custom context data (e.g., a list of books)
        context['welcome_message'] = 'Welcome to our Online Bookstore "The Black Cat"!'
        # context['books'] = Book.objects.all()  # Fetch all books from the database

        return context


class BooksListView(ListView):
    model = Book
    template_name = 'books-list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'book-details.html'


class SearchResultsListView(ListView):
    model = Book
    template_name = 'search-results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
            )


class BookCheckoutView(DetailView):
    model = Book
    template_name = 'checkout.html'
