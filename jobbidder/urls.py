from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html')),

   # path('login', views.login_user, name='login_user'),
    path('accounts/register/', views.register, name="register"),
    path('<int:company_id>/', views.detail, name='detail'),
    path('addjob', views.addjob, name='addjob'),
    path('addcompany', views.addcompany, name='addcompany'),
    path('adduser', views.adduser, name='adduser')
]
