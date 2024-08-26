from django.urls import path
from . import views

app_name = "main"   
from main.views import(
    home_screen_view,
    )

urlpatterns = [
    path("", views.home_screen_view, name="home"),
   
    path("password_reset", views.password_reset_request, name="password_reset")
    ]