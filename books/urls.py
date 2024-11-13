from django.urls import path
from books.views import HomePageView, BooksListView, BooksDetailView, SearchResultsListView, BookCheckoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('books-list/', BooksListView.as_view(), name='books-list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='book-details'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name='checkout'),
]