from django.urls import path
from books import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('books-list/', views.BooksListView.as_view(), name='books-list'),

    path('add-book/', views.BookAddView.as_view(), name='add-book'),
    path('<int:pk>/', views.BooksDetailView.as_view(), name='book-details'),
    path('books/<int:pk>/edit/', views.BookEditView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),

    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    path('<int:pk>/checkout/', views.BookCheckoutView.as_view(), name='checkout'),
    path('order-confirmation/<int:pk>/', views.OrderConfirmationView.as_view(), name='order-confirmation'),
]



