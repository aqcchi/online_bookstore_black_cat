from django.urls import path
from authors import views

urlpatterns = [
    path('authors-list/', views.AuthorsListView.as_view(), name='authors-list'),

    path('add-author/', views.AuthorAddView.as_view(), name='add-author'),
    path('author/<int:pk>/', views.AuthorsDetailView.as_view(), name='author-details'),
    path('author/<int:pk>/edit/', views.AuthorEditView.as_view(), name='author-edit'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
]