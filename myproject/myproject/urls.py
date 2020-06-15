"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from account.views import login_view, register_view, logout_view
from pages.views import home_view
from soldiers.views import (
    soldier_detail_view,
    soldier_delete_view,
    soldier_create_view,
    soldier_list_view,
    dynamic_lookup_view
    )
from irb.views import presence_create_view, presence_list_view
from search.views import search
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view),
    path('soldiers/', soldier_list_view, name='soldier-list'),
    path('soldiers/<int:id>/', dynamic_lookup_view, name='soldier'),
    path('create/', soldier_create_view),
    path('admin/', admin.site.urls),
    path('soldiers/<int:id>/delete/', soldier_delete_view, name='soldier-delete'),
    path('login/account/register/', register_view),
    path('account/logout/', logout_view),
    path('search/', search, name='search'),
    path('chat/', include('chat.urls')),
    path('irb/', presence_create_view),
    path('presence/', presence_list_view),
]+staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
