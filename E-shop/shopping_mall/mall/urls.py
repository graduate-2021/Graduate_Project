from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainView.as_view()),
    path('category/<str:name>/', views.category_page)
    #path('contact/', views.ContactView.as_view()),
]