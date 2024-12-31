from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import News, Category, Subtitle

class NewsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.news = News.objects.create(
            title="Test News",
            content="This is a test news article.",
            reporter=self.user,
            created_at="2024-01-01T00:00:00Z"
        )
        self.news_list_url = reverse('news-list')
        self.news_detail_url = reverse('news-detail', args=[self.news.id])

    def test_create_news(self):
        data = {
            "title": "New Test News",
            "content": "This is a new test news article.",
            "reporter": self.user.id
        }
        response = self.client.post(self.news_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_news_list(self):
        response = self.client.get(self.news_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_news_detail(self):
        response = self.client.get(self.news_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.news.title)

    def test_update_news(self):
        data = {
            'title': 'Updated News Article',
            'content': 'This news article has been updated.',
        }
        response = self.client.put(self.news_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_news(self):
        response = self.client.delete(self.news_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CategoryAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.category = Category.objects.create(name="Test Category")
        self.category_list_url = reverse('category-list')
        self.category_detail_url = reverse('category-detail', args=[self.category.id])

    def test_create_category(self):
        data = {"name": "New Test Category"}
        response = self.client.post(self.category_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category_list(self):
        response = self.client.get(self.category_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_category_detail(self):
        response = self.client.get(self.category_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_category(self):
        data = {"name": "Updated Test Category"}
        response = self.client.put(self.category_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Updated Test Category")

    def test_delete_category(self):
        response = self.client.delete(self.category_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())

class SubtitleAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.news = News.objects.create(
            title="Test News",
            content="This is a test news article.",
            reporter=self.user,
            created_at="2024-01-01T00:00:00Z"
        )
        self.subtitle = Subtitle.objects.create(title="Test Subtitle", news=self.news)
        self.subtitle_list_url = reverse('subtitle-list')
        self.subtitle_detail_url = reverse('subtitle-detail', args=[self.subtitle.id])

    def test_create_subtitle(self):
        data = {"title": "New Test Subtitle", "news": self.news.id}
        response = self.client.post(self.subtitle_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_subtitle_list(self):
        response = self.client.get(self.subtitle_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_subtitle_detail(self):
        response = self.client.get(self.subtitle_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.subtitle.title)

    def test_update_subtitle(self):
        data = {"title": "Updated Test Subtitle", "news": self.news.id}
        response = self.client.put(self.subtitle_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.subtitle.refresh_from_db()
        self.assertEqual(self.subtitle.title, "Updated Test Subtitle")

    def test_delete_subtitle(self):
        response = self.client.delete(self.subtitle_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subtitle.objects.filter(id=self.subtitle.id).exists())