from news import views
from . import views
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.views import(
TokenObtainPairView,
TokenRefreshView,
)
from .views import (
AdminAdvertisingViewSet,
PublicAdvertisingViewSet,
PostViewSet,
NewsViewSet,
CategoryViewSet,
NewsListView,
NewsCreateView, 
NewsDetailView,
SettingListView,
SettingCreateView,
SettingUpdateView,
AdvertisingListView,
AdvertisingCreateView,
AdvertisingUpdateView,
AdvertisingDeleteView,
UserListView,
UserCreateView,
UserUpdateDeleteView,
AddCategory,
CategoryListView,
CategoryDetailView,
DailyStatsView,
WeeklyStatsView,
ProtectedView,
AdminAdvertisingListView,
PublicAdvertisingListView,
PasswordResetRequestView,
PasswordResetView,
UserRegistrationView,
RegisterView,
RequestPasswordResetAPIView,
ResetPasswordAPIView,
subtitle_list,
add_subtitle,
edit_subtitle,
delete_subtitle,
edit_category,
delete_category,
create_news,
)
from .views import UserProfileDetailView 

schema_view = get_schema_view(
    openapi.Info(
        title="News API",
        default_version="v1",
        description="API documentation for the News application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@news.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('send-sms/',views.send_sms),
    path('verify/', views.verify_otp, name='verify_otp'),
        
    path('comment/report/<int:comment_id>/', views.report_comment, name='report_comment'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('news/create/', NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

    path('settings/', SettingListView.as_view(), name='setting-list'),
    path('settings/add/', SettingCreateView.as_view(), name='setting-create'),
    path('settings/<int:pk>/edit/', SettingUpdateView.as_view(), name='setting-update'),

    path('advertising/', AdvertisingListView.as_view(), name='advertising-list'),
    path('advertising/add/', AdvertisingCreateView.as_view(), name='advertising-create'),
    path('advertising/<int:pk>/edit/', AdvertisingUpdateView.as_view(), name='advertising-update'),
    path('advertising/<int:id>/delete/', AdvertisingDeleteView.as_view(), name='delete-advertising'),
    path('advertisements/', PublicAdvertisingListView.as_view(), name='public-advertising-list'),
    
    path('categories/add/', AddCategory.as_view(), name='category-add'),
    path('categories/edit/<int:pk>/', edit_category, name='edit-category'),
    path('categories/<int:pk>/delete/', delete_category, name='category-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('subtitles/', subtitle_list, name='subtitle-list'),
    path('subtitles/add/', add_subtitle, name='subtitle-add'),
    path('subtitles/<int:pk>/edit/', edit_subtitle, name='subtitle-edit'),
    path('subtitles/<int:pk>/delete/', delete_subtitle, name='subtitle-delete'),
    
    path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    
    path('daily/', DailyStatsView.as_view(), name='daily-stats'),
    path('weekly/', WeeklyStatsView.as_view(), name='weekly-stats'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token_create/', obtain_auth_token, name='token_create'),
    
    path('protected/', ProtectedView.as_view(), name='protected-view'),
    
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    p
    ath('custom-register/', RegisterView.as_view(), name='custom-register'),
    
    path('', include(router.urls)),
    path('api/', include(router.urls)), 
    
    path('password-reset-request/', RequestPasswordResetAPIView.as_view(), name='password-reset-request'),
    path('password-reset/<uidb64>/<token>/', ResetPasswordAPIView.as_view(), name='password-reset'),
]