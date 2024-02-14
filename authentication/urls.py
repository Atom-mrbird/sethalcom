from django.urls import path
from .views import login_user, register,logout_user,activate_user
from todo.views import index


urlpatterns = [
    path('', index, name='index'),
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path("logout_user", logout_user, name='logout_user'),
    path('activate-user/<uidb64>/<token>',
         activate_user, name='activate'),
]
