from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("contact.urls")),
    re_path('^admin/', admin.site.urls),

    re_path(r'^admin/password_reset/$',auth_views.PasswordResetView.as_view(),name='admin_password_reset'),
    re_path(r'^admin/password_reset/done/$',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    re_path(r'^reset/done/$',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    re_path(r'^password/change/$',
    auth_views.PasswordChangeView.as_view(),
    name='auth_password_change'),
    re_path(r'^password/change/done/$',
    auth_views.PasswordChangeDoneView.as_view(),
    name='auth_password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)