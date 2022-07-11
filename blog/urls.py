
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views as sitemap_views
from main.sitemaps import StaticViewSitemap, TutorialViewSitemap, PostViewSitemap

from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.storage import staticfiles_storage

from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm




sitemaps = {
    'home-page': StaticViewSitemap,
    'tutorial': TutorialViewSitemap,
    'blog':  PostViewSitemap,
}


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', include('main.urls')),
    path('noticias/', include('mainsite.urls')),
    path('news/', include('mainsite_en.urls')),
    path('en/', include('main_en.urls')),
    path('es/', include('main_es.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('django_blog_it.urls')),
    path('blog_en/', include('django_blog_it_en.urls')),
    url(r'^quiz/', include('quiz.urls')),
    path('sitemaps.xml/', sitemap, {'sitemaps': sitemaps}),
    
    path('user', include('users.urls')),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),


    path('ckeditor/', include('ckeditor_uploader.urls')),    
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




handler404 = 'main.views.error_404_view'

