from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views
from account.views import(
    login_user,
    )
from account.views import(
    logout_user,
    )
from account.views import(
    register,
    )
from account.views import(
    adminRegister,
    )
from account.views import(
    home_screen_view,
    )

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', home_screen_view, name="home"),
    path('account/', include('django.contrib.auth.urls')),
    #path('account/' , include('account.url')),
    path('login_user/' , views.login_user, name = "login"),
    path('logout_user/' , views.logout_user, name = "logout"),
    path('user_input/' , views.user_input, name = "user_input"),
    path('register/' , views.register, name = "register"),
    path('adminRegister/' , views.adminRegister, name = "adminRegister"),
#password
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authenticate/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="authenticate/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authenticate/password_reset_complete.html'), name='password_reset_complete'),      
    ]