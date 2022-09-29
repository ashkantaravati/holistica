import imp
from django.contrib import admin
from django.urls import path
from employee.views import home

urlpatterns = [path("admin/", admin.site.urls), path("", home)]
