from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Book
from common.models import Comment


class CreateCommentTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='password')
        self.book = Book.objects.create(title='Test Book')

        # URL for creating a comment
        self.create_comment_url = reverse('create-comment', kwargs={'book_id': self.book.pk})

    def test_create_comment_valid(self):
        """Test creating a comment successfully."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.create_comment_url, {'text': 'New comment text.'})
        self.assertRedirects(response, reverse('book-details', kwargs={'pk': self.book.pk}))
        self.assertEqual(Comment.objects.count(), 1)  # Comment count should increase by 1

    def test_create_comment_invalid_request(self):
        """Test invalid request for creating a comment (non-POST request)."""
        response = self.client.get(self.create_comment_url)
        self.assertEqual(response.status_code, 400)  # Invalid request
