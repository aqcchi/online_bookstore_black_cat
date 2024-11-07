from django.urls import path
from books.views import HomePageView, BooksListView, BooksDetailView, SearchResultsListView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('list/', BooksListView.as_view(), name='books-list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='book-details'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]