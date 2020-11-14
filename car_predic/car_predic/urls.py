from django.contrib import admin

from django.urls import path
from car import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('predict/',views.predict,name='predict'),
]
# r'^predict/$