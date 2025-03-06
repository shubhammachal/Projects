from django.urls import path
from . import views

#url configurations
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('counter/', views.counter, name='counter'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('months/', views.months, name='months_list'),
    path('months/<int:month_number>/', views.month_detail, name='month_detail'),

    
    ]