"""superblog URL Configuration

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
from django.urls import path
from utilisateur import views

app_name = "user"

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('inscription/', views.inscription, name='inscription'),
    path('profil/', views.profil, name='profil'),
    path('profil/update/<int:pk>/', views.UpdateUser.as_view(), name='user_update'),
    path('password/<int:pk>/', views.UpdatePassWord.as_view(), name='password_update'),
    path('avatar/<int:pk>/', views.UpdateAvatar.as_view(), name='avatar_update'),
    path('setavatar/<int:pk>', views.SetAvatar.as_view(), name="set_avatar"),
    path('role/<int:pk>', views.UpdateRole.as_view, name='role_update'),

]
