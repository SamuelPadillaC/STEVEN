from django.urls import include, path

from . import views

urlpatterns = [
    path('mail', views.mail, name='mail'),
    path('registration/', views.registration, name='registration'),
    path('students/', views.students, name='studets'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
]
