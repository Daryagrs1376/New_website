from django.core.management.base import BaseCommand
from faker import Faker
from datetime import timedelta
from django.utils import timezone
from news.models import News, Category, NewsCategory, NewsArticle, Comment, Advertising
from django.contrib.auth.models import User
from random import choice, randint
from django.utils.timezone import make_aware

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for News app'

    def handle(self, *args, **kwargs):
        fake = Faker('fa_IR')  # استفاده از زبان فارسی برای داده‌های جعلی

        # 1. ایجاد کاربران جعلی
        self.stdout.write('در حال ایجاد کاربران جعلی...')
        users = []
        for _ in range(10):  # تعداد کاربران جعلی
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'  # رمز عبور پیش‌فرض
            )
            users.append(user)
        self.stdout.write('کاربران جعلی ایجاد شد!')

        # 2. ایجاد دسته‌بندی‌های جعلی
        self.stdout.write('در حال ایجاد دسته‌بندی‌های جعلی...')
        categories = []
        for _ in range(5):  # تعداد دسته‌بندی‌های جعلی
            category = Category.objects.create(
                title=fake.word(),
                name=fake.word(),
                description=fake.text()
            )
            categories.append(category)
        self.stdout.write('دسته‌بندی‌های جعلی ایجاد شد!')

        # 3. ایجاد اخبار جعلی
        self.stdout.write('در حال ایجاد اخبار جعلی...')
        for _ in range(15):  # تعداد اخبار جعلی
            news = News.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(max_nb_chars=500),
                author=choice(users),  # اختصاص کاربر جعلی به عنوان نویسنده
                reporter=choice(users),  # اختصاص کاربر جعلی به عنوان گزارشگر
                published_date=fake.date_time_this_year(),
                status=choice(['فعال', 'غیرفعال']),
                short_description=fake.sentence(nb_words=10),
                is_approved=choice([True, False])
            )
            news.save()

            # افزودن دسته‌بندی‌ها به اخبار
            for category in categories:
                NewsCategory.objects.create(news=news, category=category)

        self.stdout.write('اخبار جعلی ایجاد شد!')

        # 4. ایجاد نظرات جعلی
        self.stdout.write('در حال ایجاد نظرات جعلی...')
        for _ in range(10):  # تعداد نظرات جعلی
            news_article = NewsArticle.objects.order_by('?').first()  # انتخاب یک مقاله خبری تصادفی
            if news_article:  # بررسی وجود مقاله خبری
                Comment.objects.create(
                    content=fake.text(max_nb_chars=200),
                    news_article=news_article,  # ارجاع به مقاله خبری
                    user=choice(users),  # اختصاص کاربر جعلی به عنوان نویسنده نظر
                    created_at=fake.date_time_this_year(),
                    approved=choice([True, False])
                )
        self.stdout.write('نظرات جعلی ایجاد شد!')


        # 5. ایجاد تبلیغات جعلی
        self.stdout.write('در حال ایجاد تبلیغات جعلی...')
        for _ in range(5):  # تعداد تبلیغات جعلی
            Advertising.objects.create(
                title=fake.sentence(),
                link=fake.url(),
                banner=fake.image_url(),
                location=fake.random_element(['header', 'sidebar', 'footer']),
                start_date=fake.date_time_this_year(),
                expiration_date=fake.date_time_this_year(),
                description=fake.text(),
                status=fake.random_element(['active', 'inactive']),
            )

        self.stdout.write('تبلیغات جعلی ایجاد شد!')

        self.stdout.write('فرایند ایجاد داده‌های جعلی به اتمام رسید!')
