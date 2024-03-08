from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_views
from users_app import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolist_views.index,name='index'),
    path('account/',include('users_app.urls')),
    path('todolist/',include('todolist_app.urls')),
    path('contact',todolist_views.contact_us,name='contact'),
    path('about',todolist_views.about_us,name='about')
]
