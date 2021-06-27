from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', admin.site.urls),
     path('', views.ObjectsView.as_view(), name='main'),
    path('registration/', views.get_register, name='register'),
    path('login/', views.email_authenticate_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('objects/', views.obj_requests, name='objects'),
    path('create/', views.obj_create, name='create'),

]
