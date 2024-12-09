from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from common.forms import CreateCommentForm
from common.models import Comment


@login_required
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

    if comment.user != request.user:
        raise PermissionDenied("You do not have permission to edit this comment.")

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

    if comment.user != request.user:
        raise PermissionDenied("You do not have permission to delete this comment.")

    # ensuring the user can only delete their own comment (already handled by template logic)
    if request.method == 'POST':
        comment.delete()
        return redirect('book-details', pk=comment.to_book.pk)

    return render(request, 'comments/delete-comment.html', {'comment': comment})