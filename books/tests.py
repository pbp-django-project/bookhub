from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, UserBook

# Create your tests here.

class BookViewsTestCase(TestCase):
    def setUp(self):
        # Create test user, books, and userbooks
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.book1 = Book.objects.create(title='Book 1', authors='Author 1', publisher='Publisher 1')
        self.book2 = Book.objects.create(title='Book 2', authors='Author 2', publisher='Publisher 2')
        
        self.user_book1 = UserBook.objects.create(title='UserBook 1', authors='UserAuthor 1', publisher='UserPublisher 1', user=self.user)
        self.user_book2 = UserBook.objects.create(title='UserBook 2', authors='UserAuthor 2', publisher='UserPublisher 2', user=self.user)
        
    def test_show_books(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('books:show-books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'UserBook 1')

    def test_search_books(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('books:search-books') + '?q=Book&filter=all')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'UserBook 1')
        
    def test_add_books(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('books:add-books'), data={
            'title': 'Book 3',
            'authors': 'Author 3',
            'publisher': 'Publisher 3'
        })
        self.assertEqual(response.status_code, 200)  # Check for a successful redirect
        
    def test_get_books(self):
        response = self.client.get(reverse('books:get-books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'Book 2')
    
    def test_get_userbooks(self):
        response = self.client.get(reverse('books:get-userbooks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'UserBook 1')
        self.assertContains(response, 'UserBook 2')
