
from django.contrib import admin
from django.urls import path, include
from guildboard import views


urlpatterns = [

    path('',views.guildboard, name="guildboard"),
    path('request',views.request, name="request"),
    path('analyzer',views.analyzer, name="analyzer"),

]
