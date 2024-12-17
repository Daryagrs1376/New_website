# استفاده از تصویر پایه پایتون نسخه 3.10
FROM python:3.10-slim

# تنظیم مسیر کاری داخل کانتینر
WORKDIR /app

# کپی کردن تمام فایل‌های پروژه به داخل کانتینر
COPY . /app

# نصب وابستگی‌های سیستمی موردنیاز
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    libz-dev \
    build-essential \
    && apt-get clean

# نصب پکیج‌های پایتون
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# اعمال پچ برای رفع مشکل haystack
COPY patches/fields.py /usr/local/lib/python3.10/site-packages/haystack/

# انجام تنظیمات اولیه Django (مفید برای جلوگیری از مشکلات اجرایی)
RUN python3 manage.py collectstatic --noinput \
    && python3 manage.py migrate --noinput

# باز کردن پورت 8000
EXPOSE 8000

# اجرای سرور Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
