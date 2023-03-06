from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('faq/', views.faq, name='faq'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/signin/', views.login, name='login'),
    path('dashboard/signup/', views.signup, name='sign-up'),
    path('dashboard/logout/', views.logout, name='logout'),
]