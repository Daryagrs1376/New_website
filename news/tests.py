from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from news.models import (
    Tokens, MyModel, Article, Media, OTP, PasswordResetToken, Post, UserProfile, 
    Subtitle, NewsCategory, Category, Keyword, Feature, Grouping, News, 
    SpecialFeature, SpecialCategory, NewsSpecialAttributes, NewsReporter, ReporterProfile, 
    UserManager, AddUserForm, NewsKeywords, AnotherModel, Role, Advertising, Setting, 
    Dashboard, PageView, Comment, Report, Like, NewsArticle, NewsComment
)
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from news.serializers import SettingCreateUpdateSerializer, AdvertisingSerializer, AdvertisingCreateUpdateSerializer

class NewsArticleTest(TestCase):
    def test_create_news_article(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        news_article = NewsArticle.objects.create(title="Test Article", content="Test Content", author=user)
        self.assertEqual(news_article.author.username, 'testuser')

class TokensModelTest(TestCase):
    def test_create_token(self):
        user = User.objects.create_user(username='testuser', password='12345')
        token = Tokens.objects.create(token='abc123', user=user)
        self.assertEqual(token.token, 'abc123')
        self.assertEqual(token.user, user)

class MyModelTest(TestCase):
    def test_create_mymodel(self):
        my_model = MyModel.objects.create(title='Test Title', description='Test Description')
        self.assertEqual(my_model.title, 'Test Title')
        self.assertEqual(my_model.description, 'Test Description')

class ArticleModelTest(TestCase):
    def test_create_article(self):
        user = User.objects.create_user(username='testuser', password='12345')
        article = Article.objects.create(title='Test Article', content='Test Content', author=user)
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.content, 'Test Content')
        self.assertEqual(article.author, user)

class MediaModelTest(TestCase):
    def test_create_media(self):
        user = User.objects.create_user(username='testuser', password='12345')
        article = Article.objects.create(title='Test Article', content='Test Content', author=user)
        media = Media.objects.create(file='uploads/testfile.jpg', article=article)
        self.assertEqual(media.file, 'uploads/testfile.jpg')
        self.assertEqual(media.article, article)

class OTPModelTest(TestCase):
    def test_create_otp(self):
        otp = OTP.objects.create(phone='1234567890')
        self.assertEqual(len(otp.code), 6)
        self.assertEqual(otp.phone, '1234567890')

class PasswordResetTokenModelTest(TestCase):
    def test_create_password_reset_token(self):
        user = User.objects.create_user(username='testuser', password='12345')
        token = PasswordResetToken.objects.create(user=user)
        self.assertEqual(token.user, user)
        self.assertFalse(token.is_used)

class PostModelTest(TestCase):
    def test_create_post(self):
        user = User.objects.create_user(username='testuser', password='12345')
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.author, user)

class UserProfileModelTest(TestCase):
    def test_create_user_profile(self):
        user = User.objects.create_user(username='testuser', password='12345')
        profile = UserProfile.objects.create(user=user, phone_number='1234567890', bio='Test Bio')
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.phone_number, '1234567890')
        self.assertEqual(profile.bio, 'Test Bio')

class SubtitleModelTest(TestCase):
    def test_create_subtitle(self):
        subtitle = Subtitle.objects.create(title='Test Title', subtitle_title='Test Subtitle', description='Test Description')
        self.assertEqual(subtitle.title, 'Test Title')
        self.assertEqual(subtitle.subtitle_title, 'Test Subtitle')
        self.assertEqual(subtitle.description, 'Test Description')

class NewsCategoryModelTest(TestCase):
    def test_create_news_category(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=User.objects.create_user(username='author', password='12345'), reporter=reporter, published_date=timezone.now())
        category = Category.objects.create(title='Test Category', name='Test Name', description='Test Description')
        news_category = NewsCategory.objects.create(news=news, category=category)
        self.assertEqual(news_category.news, news)
        self.assertEqual(news_category.category, category)

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(title='Test Category', name='Test Name', description='Test Description')
        self.assertEqual(category.title, 'Test Category')
        self.assertEqual(category.name, 'Test Name')
        self.assertEqual(category.description, 'Test Description')

class KeywordModelTest(TestCase):
    def test_create_keyword(self):
        category = Category.objects.create(title='Test Category', name='Test Name', description='Test Description')
        keyword = Keyword.objects.create(word='Test Keyword', category=category)
        self.assertEqual(keyword.word, 'Test Keyword')
        self.assertEqual(keyword.category, category)

class FeatureModelTest(TestCase):
    def test_create_feature(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=User.objects.create_user(username='author', password='12345'), reporter=reporter, published_date=timezone.now())
        feature = Feature.objects.create(feature_name='Test Feature', news=news)
        self.assertEqual(feature.feature_name, 'Test Feature')
        self.assertEqual(feature.news, news)

class GroupingModelTest(TestCase):
    def test_create_grouping(self):
        grouping = Grouping.objects.create(Grouping_name='Test Grouping')
        self.assertEqual(grouping.Grouping_name, 'Test Grouping')

class NewsModelTest(TestCase):
    def test_create_news(self):
        author = User.objects.create_user(username='author', password='12345')
        reporter = User.objects.create_user(username='reporter', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=author, reporter=reporter, published_date=timezone.now())
        self.assertEqual(news.title, 'Test News')
        self.assertEqual(news.content, 'Test Content')
        self.assertEqual(news.author, author)
        self.assertEqual(news.reporter, reporter)

class SpecialFeatureModelTest(TestCase):
    def test_create_special_feature(self):
        special_feature = SpecialFeature.objects.create(feature_name='Test Special Feature')
        self.assertEqual(special_feature.feature_name, 'Test Special Feature')

class SpecialCategoryModelTest(TestCase):
    def test_create_special_category(self):
        special_category = SpecialCategory.objects.create(category_name='Test Special Category')
        self.assertEqual(special_category.category_name, 'Test Special Category')

class NewsSpecialAttributesModelTest(TestCase):
    def test_create_news_special_attributes(self):
        special_feature = SpecialFeature.objects.create(feature_name='Test Special Feature')
        special_category = SpecialCategory.objects.create(category_name='Test Special Category')
        special_attributes = NewsSpecialAttributes.objects.create(special_feature1=special_feature, special_category1=special_category)
        self.assertEqual(special_attributes.special_feature1, special_feature)
        self.assertEqual(special_attributes.special_category1, special_category)

class NewsReporterModelTest(TestCase):
    def test_create_news_reporter(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        category = Category.objects.create(title='Test Category', name='Test Name', description='Test Description')
        news_reporter = NewsReporter.objects.create(reporter=reporter, category=category, title='Test Title', news_text='Test News Text')
        self.assertEqual(news_reporter.reporter, reporter)
        self.assertEqual(news_reporter.category, category)
        self.assertEqual(news_reporter.title, 'Test Title')
        self.assertEqual(news_reporter.news_text, 'Test News Text')

class ReporterProfileModelTest(TestCase):
    def test_create_reporter_profile(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        profile = ReporterProfile.objects.create(reporter=reporter, phone='1234567890')
        self.assertEqual(profile.reporter, reporter)
        self.assertEqual(profile.phone, '1234567890')

class UserManagerTest(TestCase):
    def test_create_user(self):
        user_manager = UserManager()
        user = user_manager.create_user(phone_number='1234567890', password='12345')
        self.assertEqual(user.phone_number, '1234567890')

    def test_create_superuser(self):
        user_manager = UserManager()
        superuser = user_manager.create_superuser(phone_number='1234567890', password='12345')
        self.assertTrue(superuser.is_admin)

class AddUserFormTest(TestCase):
    def test_add_user_form(self):
        form_data = {'username': 'testuser', 'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'}
        form = AddUserForm(data=form_data)
        self.assertTrue(form.is_valid())

class NewsKeywordsModelTest(TestCase):
    def test_create_news_keywords(self):
        category = Category.objects.create(title='Test Category', name='Test Name', description='Test Description')
        reporter = User.objects.create_user(username='reporter', password='12345')
        news_reporter = NewsReporter.objects.create(reporter=reporter, category=category, title='Test Title', news_text='Test News Text')
        self.assertEqual(news_reporter.reporter, reporter)
        self.assertEqual(news_reporter.category, category)
        self.assertEqual(news_reporter.title, 'Test Title')
        self.assertEqual(news_reporter.news_text, 'Test News Text')

class AnotherModelTest(TestCase):
    def test_create_another_model(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=User.objects.create_user(username='author', password='12345'), reporter=reporter, published_date=timezone.now())
        another_model = AnotherModel.objects.create(news=news)
        self.assertEqual(another_model.news, news)

class RoleModelTest(TestCase):
    def test_create_role(self):
        role = Role.objects.create(name=Role.ADMIN)
        self.assertEqual(role.name, Role.ADMIN)

class AdvertisingModelTest(TestCase):
    def test_create_advertising(self):
        advertising = Advertising.objects.create(title='Test Advertising', link='http://example.com', location='header', start_date=timezone.now(), description='Test Description')
        self.assertEqual(advertising.title, 'Test Advertising')
        self.assertEqual(advertising.link, 'http://example.com')
        self.assertEqual(advertising.location, 'header')
        self.assertEqual(advertising.description, 'Test Description')

class SettingModelTest(TestCase):
    def test_create_setting(self):
        setting = Setting.objects.create(subcategory_name='Test Setting', contact_us='Test Contact Us', about_us='Test About Us')
        self.assertEqual(setting.subcategory_name, 'Test Setting')
        self.assertEqual(setting.contact_us, 'Test Contact Us')
        self.assertEqual(setting.about_us, 'Test About Us')

class DashboardModelTest(TestCase):
    def test_create_dashboard(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=User.objects.create_user(username='author', password='12345'), reporter=reporter, published_date=timezone.now())
        dashboard = Dashboard.objects.create(news=news)
        self.assertEqual(dashboard.news, news)

class PageViewModelTest(TestCase):
    def test_create_page_view(self):
        page_view = PageView.objects.create(date=timezone.now().date(), total_visits=100, social_visits=50, bounce_rate=0.5, page_views={})
        self.assertEqual(page_view.total_visits, 100)
        self.assertEqual(page_view.social_visits, 50)
        self.assertEqual(page_view.bounce_rate, 0.5)
        self.assertEqual(page_view.page_views, {})

class CommentModelTest(TestCase):
    def test_create_comment(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        user = User.objects.create_user(username='testuser', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=user, reporter=reporter, published_date=timezone.now())
        news_article = NewsArticle.objects.create(title='Test Article', content='Test Content', author=user)
        comment = Comment.objects.create(author=user, news=news, news_article=news_article, content='Test Comment')
        self.assertEqual(comment.author, user)
        self.assertEqual(comment.news, news)
        self.assertEqual(comment.news_article, news_article)
        self.assertEqual(comment.content, 'Test Comment')

class ReportModelTest(TestCase):
    def test_create_report(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        user = User.objects.create_user(username='testuser', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=user, reporter=reporter, published_date=timezone.now())
        news_article = NewsArticle.objects.create(title='Test Article', content='Test Content', author=user)
        comment = Comment.objects.create(author=user, news=news, news_article=news_article, content='Test Comment')
        report = Report.objects.create(user=user, comment=comment, reason='Test Reason')
        self.assertEqual(report.user, user)
        self.assertEqual(report.comment, comment)
        self.assertEqual(report.reason, 'Test Reason')

class LikeModelTest(TestCase):
    def test_create_like(self):
        user = User.objects.create_user(username='testuser', password='12345')
        news_article = NewsArticle.objects.create(title='Test Article', content='Test Content', author=user)
        like = Like.objects.create(user=user, news_article=news_article)
        self.assertEqual(like.user, user)
        self.assertEqual(like.news_article, news_article)

class NewsArticleModelTest(TestCase):
    def test_create_news_article(self):
        user = User.objects.create_user(username='testuser', password='12345')
        news_article = NewsArticle.objects.create(title='Test Article', content='Test Content', author=user)
        self.assertEqual(news_article.title, 'Test Article')
        self.assertEqual(news_article.content, 'Test Content')
        self.assertEqual(news_article.author, user)

class NewsCommentModelTest(TestCase):
    def test_create_news_comment(self):
        reporter = User.objects.create_user(username='reporter', password='12345')
        user = User.objects.create_user(username='testuser', password='12345')
        news = News.objects.create(title='Test News', content='Test Content', author=user, reporter=reporter, published_date=timezone.now())
        news_comment = NewsComment.objects.create(content='Test Comment', news=news, user=user)
        self.assertEqual(news_comment.content, 'Test Comment')
        self.assertEqual(news_comment.news, news)
        self.assertEqual(news_comment.user, user)

class SettingUpdateViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.setting = Setting.objects.create(subcategory_name='Test Setting', contact_us='Test Contact Us', about_us='Test About Us')
        self.url = reverse('setting-update', kwargs={'pk': self.setting.pk})

    def test_update_setting(self):
        data = {'subcategory_name': 'Updated Setting', 'contact_us': 'Updated Contact Us', 'about_us': 'Updated About Us'}
        response = self.client.put(self.url, data, format='json')
        self.setting.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.setting.subcategory_name, 'Updated Setting')
        self.assertEqual(self.setting.contact_us, 'Updated Contact Us')
        self.assertEqual(self.setting.about_us, 'Updated About Us')

class AdvertisingListViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('advertising-list')
        Advertising.objects.create(title='Ad 1', location='header', status='active')
        Advertising.objects.create(title='Ad 2', location='footer', status='inactive')

    def test_list_advertising(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class AdvertisingCreateViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = reverse('advertising-create')

    def test_create_advertising(self):
        data = {'title': 'New Ad', 'location': 'sidebar', 'status': 'active', 'description': 'Test Description'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertising.objects.count(), 1)
        self.assertEqual(Advertising.objects.get().title, 'New Ad')

class AdvertisingUpdateViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.advertising = Advertising.objects.create(title='Ad 1', location='header', status='active')
        self.url = reverse('advertising-update', kwargs={'pk': self.advertising.pk})

    def test_update_advertising(self):
        data = {'title': 'Updated Ad', 'location': 'footer', 'status': 'inactive', 'description': 'Updated Description'}
        response = self.client.put(self.url, data, format='json')
        self.advertising.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.advertising.title, 'Updated Ad')
        self.assertEqual(self.advertising.location, 'footer')
        self.assertEqual(self.advertising.status, 'inactive')
        self.assertEqual(self.advertising.description, 'Updated Description')
