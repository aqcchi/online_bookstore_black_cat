from django.test import TestCase
from authors.models import Author
from common.forms import CreateCommentForm
from common.models import Comment
from books.models import Book
from accounts.models import User


class CreateCommentFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.author = Author.objects.create(first_name="Author First name", last_name="Author Last Name")

        self.book = Book.objects.create(title="Test Book")
        self.book.authors.add(self.author)  # adding author to the book

    def test_valid_form(self):
        # testing form is valid with appropriate data
        form_data = {
            'text': 'This is a valid comment.',
        }
        form = CreateCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_length(self):
        # testing form is invalid when comment is too long
        form_data = {
            'text': 'x' * 501,  # exceeding 500 characters
        }
        form = CreateCommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('text', form.errors)

    def test_form_save(self):
        # testing form can save valid comment
        form_data = {
            'text': 'This is a valid comment.',
        }
        form = CreateCommentForm(data=form_data)
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        comment.user = self.user
        comment.to_book = self.book
        comment.save()
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().text, 'This is a valid comment.')
