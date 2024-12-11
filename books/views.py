from django.core.cache import cache
from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Value
from books.forms import BookAddForm, BookEditForm
from books.models import Book, Order
from common.forms import CreateCommentForm
from common.mixins import StaffOrSuperuserMixin


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        # getting the default context
        context = super().get_context_data(**kwargs)

        # adding custom context data
        context['welcome_message'] = '''
            <h1>Welcome to our Online Bookstore "The Black Cat"!</h1>
            <p>The bookstore is named after Edgar Allan Poe’s short story of the same name – The Black Cat, and it is the perfect place for curious people who love books... and cats.</p>
            <p>Books and cats... what more does a person need in order to be happy?!</p>
            <p>The bookstore is a small family business that we embarked on with a lot of love and enthusiasm, with the hope that there are still people who prefer physical books over e-readers. Our hopes were fulfilled, and now we are happy to announce we have a large number of regular customers who visit us weekly, even daily.</p>
            <p>We hope you will also become a part of our book-loving family!</p>
            <p>Come visit us! :)</p>
        '''

        return context


class BooksListView(ListView):
    model = Book
    template_name = 'books-list.html'


class BookAddView(LoginRequiredMixin, StaffOrSuperuserMixin, CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'books/book-add.html'
    success_url = reverse_lazy('books-list')


class BookEditView(LoginRequiredMixin, StaffOrSuperuserMixin, UpdateView):
    model = Book
    form_class = BookEditForm
    template_name = 'books/book-edit.html'

    def get_success_url(self):
        return reverse_lazy('book-details', kwargs={'pk': self.object.pk})


class BookDeleteView(LoginRequiredMixin, StaffOrSuperuserMixin, DeleteView):
    model = Book
    template_name = 'books/book-delete.html'
    success_url = reverse_lazy('books-list')


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

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Book.objects.none()

        return Book.objects.annotate(
            full_name=Concat('authors__first_name', Value(' '), 'authors__last_name')
        ).filter(
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query) |
            Q(full_name__icontains=query)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['object_list']
        return context


class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url = 'login'
    context_object_name = 'book'

    def post(self, request, *args, **kwargs):

        book = self.get_object()

        if not book.book_available:
            messages.error(request, "This book is currently out of stock.")
            return redirect('book-details', pk=book.pk)

        order = Order.objects.create(
            ordered_book=book,
            user=request.user,
            amount_paid=book.price
        )

        book.book_available = False
        book.save()

        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmationView(DetailView):
    model = Order
    template_name = 'order-confirmation.html'
    context_object_name = 'order'

    def get(self, request, *args, **kwargs):
        order = self.get_object()

        order.is_completed = True
        order.save()

        # updating the cache directly (optional)
        total_sales = cache.get('total_sales', 0)
        total_sales += order.amount_paid
        cache.set('total_sales', total_sales)

        return render(request, self.template_name, {'order': order})


def total_sales_view(request):
    if not request.user.is_superuser:
        # If user != superuser, redirect to a different page
        messages.error(request, "You do not have permission to view this page.")
        return redirect('homepage')

    # retrieving total sales from cache
    total_sales = cache.get('total_sales', 0)

    return render(request, 'total-sales.html', {'total_sales': total_sales})