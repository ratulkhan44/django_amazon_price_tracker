
from django.contrib import admin
from django.urls import path
from links.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home_view"),
]
