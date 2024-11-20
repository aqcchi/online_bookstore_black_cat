from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Book
from common.forms import CreateCommentForm
from common.models import Comment


def create_comment(request, book_id: int):
    if request.POST:
        book = Book.objects.get(pk=book_id)
        comment_form = CreateCommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_book = book
            comment.user = request.user
            comment.save()

        return redirect('book-details', pk=book_id)
    else:
        return HttpResponse("Invalid request", status=400)
        #  makes sure only POST requests get through; safety


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # user can only edit their own comment (already handled by template logic)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('book-details', pk=comment.to_book.pk)
    else:
        form = CreateCommentForm(instance=comment)  # populating form with current comment data

    # updating template path to match new directory
    return render(request, 'comments/edit-comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # ensuring the user can only delete their own comment (already handled by template logic)
    if request.method == 'POST':
        comment.delete()  # Delete the comment
        return redirect('book-details', pk=comment.to_book.pk)

    return render(request, 'comments/delete-comment.html', {'comment': comment})