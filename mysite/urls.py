"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from account import views
from django.conf import settings
from django.conf.urls.static import static
from account.views import(
    login_user,
    )
from account.views import(
    adminLogin,
    )
from account.views import(
    register,
    )
#from account.views import(
  #  deleteUser,
   # )
from account.views import(
    adminRegister,
    )
from main.views import(
    home_screen_view,
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('account/' , include('account.urls')),
    path('account/' , include('django.contrib.auth.urls')),
    path('login_user/' , views.login_user, name = "login"),
    path('adminLogin/' , views.adminLogin, name = "adminLogin"),
    path('register/' , views.register, name = "register"),
    #path('deleteUser/' , views.deleteUser, name = "deleteUser"),
    path('adminRegister/' , views.adminRegister, name = "adminRegister"),
    path('logout_user/' , views.logout_user, name = "logout"),
    path('user_input/', views.user_inputp,name="user_input"),
    path('user_output/', views.user_output,name="user_output"),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
   #urlpatterns += STATIC(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)