from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import token
from django.contrib.auth.models import User
from .models import News, Category, Subtitle


class NewsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='token ' + self.token.key)
                self.news = News.objects.create(
            title="Test News",
            content="This is a test news article.",
            reporter=self.user, 
            created_at="2024-01-01T00:00:00Z"
        )

    def test_create_news(self):
        url = reverse('news-list')
        data = {
            "title": "New Test News",
            "content": "This is a new test news article.",
            "reporter": self.user.id
        }
        response = self.client.post(url, data, format='json')
        print(response.data) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_news_list(self):
        url = reverse('news-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_get_news_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION='token ' + self.token.key)

        url = reverse('news-detail', args=[self.news.id])
        response = self.client.get(url)
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.news.title)

    def test_update_news(self):
        url = reverse('news-detail', args=[self.news.id])
        data = {
            'title': 'Updated News Article',
            'content': 'This news article has been updated.',
        }
        response = self.client.put(url, data, format='json')
        print(response.data) 
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_news(self):
        url = reverse('news-detail', args=[self.news.id])
        response = self.client.delete(url)
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CategoryAPITest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='token ' + self.token.key)
        self.category = Category.objects.create(name="Test Category", description="Test Description")

    def test_create_category(self):
        url = reverse('category-list')
        data = {
            'name': 'New Test Category',
            'description': 'Description of new test category',
        }
        response = self.client.post(url, data, format='json')
        print(response.data) 
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_category_list(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_category_detail(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_category(self):
        url = reverse('category-detail', args=[self.category.id])
        data = {'name': 'Updated Category', 'description': 'Updated description'}
        response = self.client.put(url, data, format='json')
        print(response.data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SubtitleAPITest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='token ' + self.token.key)
        self.subtitle = Subtitle.objects.create(title="Test Subtitle")

    def test_create_subtitle(self):
        url = reverse('subtitle-list')
        data = {
            'title': 'New Subtitle',
            'description': 'This is a new subtitle for testing.'
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_subtitle_list(self):
        url = reverse('subtitle-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_subtitle_detail(self):
        url = reverse('subtitle-detail', args=[self.subtitle.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.subtitle.title)

    def test_update_subtitle(self):
        url = reverse('subtitle-detail', args=[self.subtitle.id])
        data = {'title': 'Updated Subtitle', 'description': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        print(response.data)  
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_subtitle(self):
        url = reverse('subtitle-detail', args=[self.subtitle.id])
        response = self.client.delete(url)
        print(response.data)  
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
