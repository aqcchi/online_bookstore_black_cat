from django.urls import path
from common import views

urlpatterns = [
    path('comment/<int:book_id>/', views.create_comment, name='create-comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit-comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete-comment'),
]