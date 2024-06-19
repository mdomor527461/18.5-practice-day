from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.register, name = 'register'),
    path('login/',views.user_login, name = 'user_login'),
    path('logout/',views.user_logout, name = 'user_logout'),
    path('profile/',views.profile, name = 'profile'),
    path('change_password/',views.passchange, name = 'passchange'),
    path('change_password_without_old_password/',views.passchange2, name = 'passchange2')
]