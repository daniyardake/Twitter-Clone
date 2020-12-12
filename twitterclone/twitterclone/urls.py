"""twitterclone URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about
from accounts.views import login, register, users, signout, user, my_account
from twits.views import twits, twit, add_twit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('users/', users, name = 'users'),
    path('signout/', signout, name = 'signout'),
    path('users/<str:login>/', user, name = 'user'),
    path('account/', my_account, name = 'my_account'),
    path('twits/', twits, name = 'twits'),
    path('twits/<int:pk>', twit, name = 'twit'),
    path('twits/add', add_twit, name = 'add_twit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

