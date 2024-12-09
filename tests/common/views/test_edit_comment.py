from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Book
from common.models import Comment


class EditCommentTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='otheruser', password='password')

        self.book = Book.objects.create(title='Test Book')
        self.comment = Comment.objects.create(user=self.user, to_book=self.book, text='Test comment')

        # URLs for editing a comment
        self.edit_comment_url = reverse('edit-comment', kwargs={'comment_id': self.comment.pk})

    def test_edit_comment_valid(self):
        """Test editing a comment successfully."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.edit_comment_url, {'text': 'Updated comment text.'})
        self.assertRedirects(response, reverse('book-details', kwargs={'pk': self.book.pk}))
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.text, 'Updated comment text.')

    def test_edit_comment_unauthorized(self):
        """Test that a user can't edit someone else's comment."""
        self.client.login(username='otheruser', password='password')
        response = self.client.post(self.edit_comment_url, {'text': 'Updated comment text.'})
        self.assertEqual(response.status_code, 403)

    def test_edit_comment_get(self):
        """Test GET request for editing a comment."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.edit_comment_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comment.text)  # form should be prepopulated with comment text
