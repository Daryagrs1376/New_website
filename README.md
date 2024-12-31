# پروژه بک‌اند پلتفرم خبرگزاری#

این پروژه شامل بک‌اند یک پلتفرم خبرگزاری است که با استفاده از Django و Django REST Framework توسعه داده شده است. هدف این پروژه ارائه یک سیستم کامل برای مدیریت اخبار، کاربران، جستجو و دسته‌بندی محتوا است.

# ویژگی‌های پروژه:

**احراز هویت کاربران**:
  - ثبت‌نام و ورود امن با استفاده از JWT (توکن‌های وب JSON) از طریق پکیج SimpleJWT.

**مدیریت اخبار**:
  - امکان ایجاد، خواندن، ویرایش و حذف خبرها، دسته‌بندی‌ها و برچسب‌ها.

**جستجو و فیلتر پیشرفته**:
  - قابلیت جستجوی متنی کامل با استفاده از Haystack و فیلتر کردن بر اساس دسته‌بندی با پکیج django-filters.

**پشتیبانی از CORS**:
  - تنظیم شده برای مدیریت درخواست‌های کراس اوریجین با django-cors-headers.

**صف وظایف غیرهمزمان**:
  - انجام وظایف پس‌زمینه با استفاده از Celery و Redis.

**مستندسازی API**:
  - مستندات تعاملی با استفاده از پکیج drf-yasg.

**مدیریت تصاویر**:
  - پردازش و بهینه‌سازی تصاویر با استفاده از کتابخانه Pillow.

**گسترش پنل مدیریت**:
  - امکانات بیشتر برای مدیریت با استفاده از django-extensions.

# نصب و راه‌اندازی#

# پیش‌نیازها:

- Python 3.8 یا بالاتر
- Django 3.2 یا بالاتر
- PostgreSQL یا SQLite

# مراحل نصب:

1. مخزن پروژه را کلون کنید:
   git clone https://github.com/Daryagrs1376/repository.git
   cd repository

2. ایجاد محیط مجازی:
python -m venv env

3. فعال‌سازی محیط مجازی:

در لینوکس:
source env/bin/activate

در ویندوز:
env\Scripts\activate

4.نصب وابستگی‌ها:
pip install -r requirements.txt

5.تنظیمات پایگاه داده را در فایل settings.py پیکربندی کنید.

6. اعمال مهاجرت‌های پایگاه داده:
python manage.py migrate

7.ایجاد ابرکاربر:
python manage.py createsuperuser

8.اجرای سرور توسعه:
python manage.py runserver

# نوع احراز هویت :
برای احراز هویت کاربران از JWT استفاده می‌شود. برای دریافت توکن، درخواست POST به /api/token/ ارسال کنید.

# مدیریت اخبار:
API‌های مربوط به مدیریت اخبار شامل ایجاد، خواندن، ویرایش و حذف خبرها، دسته‌بندی‌ها و برچسب‌ها در دسترس هستند.

# ایجاد خبر جدید:
POST /api/news/

# مشاهده لیست اخبار:
GET /api/news/

# مشاهده جزئیات خبر خاص:
GET /api/news/<id>/

# ویرایش خبر:
PUT /api/news/<id>/

# حذف خبر:
DELETE /api/news/<id>/

# جستجو و فیلتر:
برای جستجوی متنی کامل و فیلتر کردن بر اساس دسته‌بندی از API‌های مربوطه استفاده کنید.

# جستجو در اخبار:
GET /api/news/?search=<query>

# فیلتر بر اساس دسته‌بندی:
GET /api/news/?category=<category_id>


# مستندات API:
برای اطلاعات بیشتر به مستندات Swagger در مسیر /swagger/ مراجعه کنید.


# لیست پکیج‌ها و دستورات نصب:
در ادامه لیستی از تمام پکیج‌های استفاده شده در پروژه همراه با نسخه‌ی به‌روز و دستور نصب هر پکیج آورده شده است. 
این دستورها را می‌توانید به صورت جداگانه اجرا کنید یا در فایل requirements.txt قرار دهید.

asgiref: 3.8.2 ==> pip install asgiref==3.8.2
Django: 5.2 ==> pip install Django==5.2
djangorestframework: 3.16.0 ==> pip install djangorestframework==3.16.0
sqlparse: 0.5.4 ==> pip install sqlparse==0.5.4
tzdata: 2024.4 ==> pip install tzdata==2024.4
django-cors-headers: 4.8.0 ==> pip install django-cors-headers==4.8.0
drf-yasg: 1.21.9 ==> pip install drf-yasg==1.21.9
django-extensions: 3.2.5 ==> pip install django-extensions==3.2.5
djangorestframework-simplejwt: 5.4.1 ==> pip install djangorestframework-simplejwt==5.4.1
pillow: 11.1.0 ==> pip install Pillow==11.1.0
django-filters: 24.5 ==> pip install django-filters==24.5
celery: 5.3.0 ==> pip install celery==5.3.0
django-haystack: 3.1 ==> pip install django-haystack==3.1
kavenegar: 1.2.6 ==> pip install kavenegar==1.2.6

# مشارکت:
اگر مایل به مشارکت در این پروژه هستید، لطفاً یک فورک از مخزن بگیرید و تغییرات خود را در یک شاخه جدید اعمال کنید. سپس یک Pull Request ارسال کنید.

# لایسنس:
این پروژه تحت لایسنس MIT منتشر شده است. برای اطلاعات بیشتر فایل LICENSE را مشاهده کنید.

# منابع:

_ مستندات Django REST Framework

# نویسنده پروژه:

*زهرا گروسی*