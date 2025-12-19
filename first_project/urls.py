"""
Definition of urls for first_project.
"""
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path, include

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/',views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('home3/', views.home3, name='home3'),
    path('ilmiy_ishlari/<int:user_id>/', views.ilmiy_ishlari, name='ilmiy_ishlari'),
    path('ilmiy_ishlari2/<int:user_id>/', views.ilmiy_ishlari2, name='ilmiy_ishlari2'),
    path('ilmiy_ishlari3/<int:user_id>/', views.ilmiy_ishlari3, name='ilmiy_ishlari3'),
    path('oquv_ishlari2/<int:user_id>/', views.oquv_ishlari2, name='oquv_ishlari2'),
    path('oquv_ishlari3/<int:user_id>/', views.oquv_ishlari3, name='oquv_ishlari3'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile2/<int:user_id>/', views.profile2, name='profile2'),
    path('profile3/<int:user_id>/', views.profile3, name='profile3'),
    path('admin', admin.site.urls),
    path('oquv_ishlari/<int:user_id>/', views.oquv_ishlari, name='oquv_ishlari'),
    path('qoshish/<int:user_id>/',views.qoshish, name='qoshish'),
    path('qoshish_i/<int:user_id>/',views.qoshish_i, name='qoshish_i'),
    path('qoshish_oquv/<int:user_id>/',views.qoshish_oquv, name='qoshish_oquv'),
    path('qoshish_ilmiy/<int:user_id>/',views.qoshish_ilmiy, name='qoshish_ilmiy'),
    path('ochir/<int:j_id>/<int:user_id>/',views.ochir, name='ochir'),
    path('ochirish/<int:i_id>/<int:j_id>/<int:user_id>/', views.ochirish, name='ochirish'),
    path('filtrlash_ilmiy/<int:user_id>/',views.filtrlash_ilmiy, name='filtrlash_ilmiy'),
    path('filtrlash_ilmiy2/<int:user_id>/',views.filtrlash_ilmiy2, name='filtrlash_ilmiy2'),
    path('filtrlash_ilmiy3/<int:user_id>/',views.filtrlash_ilmiy3, name='filtrlash_ilmiy3'),
    path('filtrlash_oquv/<int:user_id>/',views.filtrlash_oquv, name='filtrlash_oquv'),
    path('filtrlash_oquv2/<int:user_id>/',views.filtrlash_oquv2, name='filtrlash_oquv2'),
    path('filtrlash_oquv3/<int:user_id>/',views.filtrlash_oquv3, name='filtrlash_oquv3'),
    path('tahrirlash_ilmiy/<int:i_id>/<int:t_id>/<int:user_id>/', views.tahrirlash_ilmiy, name='tahrirlash_ilmiy'),
    path('download-zip/', views.download_zip, name='download_zip'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
