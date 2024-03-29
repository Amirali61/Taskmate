from django.urls import path
import users_app.views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
